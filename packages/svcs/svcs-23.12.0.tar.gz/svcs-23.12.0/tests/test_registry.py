# SPDX-FileCopyrightText: 2023 Hynek Schlawack <hs@ox.cx>
#
# SPDX-License-Identifier: MIT

import contextlib
import inspect
import logging

from unittest.mock import AsyncMock, Mock

import pytest

import svcs

from .fake_factories import (
    async_int_factory,
    async_str_cleanup_factory,
    int_factory,
    str_cleanup_factory,
)
from .ifaces import AnotherService, Interface, Service


needs_working_async_mock = pytest.mark.skipif(
    not inspect.iscoroutinefunction(AsyncMock()),
    reason="AsyncMock not working",
)


class TestRegistry:
    def test_repr_empty(self, registry):
        """
        repr of an empty registry says 0 registered services.
        """
        assert "<svcs.Registry(num_services=0)>" == repr(registry)

    def test_repr_counts(self, registry):
        """
        repr counts 2 registered services as 2.
        """
        registry.register_factory(Service, Service)
        registry.register_factory(AnotherService, AnotherService)

        assert "<svcs.Registry(num_services=2)>" == repr(registry)

    def test_empty_close(self):
        """
        Closing an empty registry does nothing.
        """
        svcs.Registry().close()

        with svcs.Registry():
            ...

    def test_close_closes(self, registry):
        """
        Calling close on Registry runs all on_close callbacks.
        """
        close_1 = Mock()
        close_2 = Mock()

        registry.register_factory(Service, Service, on_registry_close=close_1)
        registry.register_value(
            AnotherService, AnotherService, on_registry_close=close_2
        )

        registry.close()

        assert close_1.called
        assert close_2.called
        assert not registry._services
        assert not registry._on_close

    def test_overwritten_factories_are_not_forgotten(self, registry):
        """
        If a factory is overwritten, it's close callback is still called.
        """
        close_1 = Mock()
        close_2 = Mock()

        registry.register_factory(Service, Service, on_registry_close=close_1)
        registry.register_value(
            Service, AnotherService, on_registry_close=close_2
        )

        registry.close()

        assert close_1.called
        assert close_2.called

    def test_close_warns_about_async(self, registry):
        """
        Calling close raises a warning if there are async cleanups.
        """

        async def callback():
            ...

        registry.register_factory(Service, Service, on_registry_close=callback)

        with pytest.warns(
            UserWarning,
            match="Skipped async cleanup for 'tests.ifaces.Service'.",
        ):
            registry.close()

    def test_register_factory_logs(self, registry, caplog):
        """
        register_factory logs the registration to debug.
        """
        caplog.set_level(logging.DEBUG)

        registry.register_factory(Interface, Service)

        assert [
            "registered factory <class 'tests.ifaces.Service'> for "
            "service type tests.ifaces.Interface"
        ] == caplog.messages
        assert "tests.ifaces.Interface" == caplog.records[0].svcs_service_name
        assert "tests.ifaces.Service" == caplog.records[0].svcs_factory_name

    def test_register_value_logs(self, registry, caplog):
        """
        register_value logs the registration to debug.
        """
        caplog.set_level(logging.DEBUG)

        registry.register_value(Service, 42)

        assert [
            "registered value 42 for service type tests.ifaces.Service"
        ] == caplog.messages
        assert "tests.ifaces.Service" == caplog.records[0].svcs_service_name
        assert 42 == caplog.records[0].svcs_value

    def test_close_logs_failures(self, registry, caplog):
        """
        Closing failures are logged but ignored.
        """
        registry.register_factory(
            Service, Service, on_registry_close=Mock(side_effect=ValueError())
        )

        with registry:
            ...

        assert [
            "Registry's on_registry_close callback failed for 'tests.ifaces.Service'."
        ] == caplog.messages
        assert "tests.ifaces.Service" == caplog.records[0].svcs_service_name

    def test_context_manager(self):
        """
        The registry is also a context manager that closes on exit.
        """
        orc = Mock()

        with svcs.Registry() as registry:
            registry.register_factory(Service, Service, on_registry_close=orc)

        orc.assert_called_once_with()

    @pytest.mark.asyncio()
    async def test_async_context_manager(self):
        """
        The registry is also an async context manager that acloses on exit.

        Passing an awaitable to on_registry_close works.
        """
        closed = False

        async def closer():
            nonlocal closed
            closed = True

        async with svcs.Registry() as registry:
            registry.register_factory(
                Service, Service, on_registry_close=closer()
            )

        assert closed

    def test_detects_async_factories(self, registry):
        """
        The is_async property of the RegisteredService is True if the factory
        needs to be awaited.
        """

        registry.register_factory(int, async_int_factory)
        registry.register_factory(str, async_str_cleanup_factory)

        assert (
            svcs.RegisteredService(int, async_int_factory, False, True, None)
            == registry._services[int]
        )
        assert (
            svcs.RegisteredService(
                str, async_str_cleanup_factory, False, True, None
            )
            == registry._services[str]
        )

    def test_no_false_positive_async(self, registry):
        """
        is_async is False for sync factories.
        """
        registry.register_factory(int, int_factory)
        registry.register_factory(str, str_cleanup_factory)

        assert (
            svcs.RegisteredService(int, int_factory, False, False, None)
            == registry._services[int]
        )
        assert (
            svcs.RegisteredService(
                str, str_cleanup_factory, False, False, None
            )
            == registry._services[str]
        )

    @pytest.mark.skipif(
        not hasattr(contextlib, "aclosing"),
        reason="Hasn't contextlib.aclosing()",
    )
    @pytest.mark.asyncio()
    async def test_async_empty_close(self, registry):
        """
        Asynchronously closing an empty registry does nothing.
        """
        await registry.aclose()

        async with svcs.Registry():
            ...

    @pytest.mark.asyncio()
    @needs_working_async_mock
    async def test_aclose_mixed(self, registry):
        """
        aclose() closes all services, including async ones.
        """
        sync_close = Mock()
        async_close = AsyncMock()

        registry.register_factory(
            Service, Service, on_registry_close=sync_close
        )
        registry.register_factory(
            AnotherService, AnotherService, on_registry_close=async_close
        )

        await registry.aclose()

        assert sync_close.called

        async_close.assert_awaited_once()

    @pytest.mark.asyncio()
    @needs_working_async_mock
    async def test_aclose_logs_failures(self, registry, caplog):
        """
        Async closing failures are logged but ignored.
        """
        close_mock = AsyncMock(side_effect=ValueError())

        registry.register_factory(
            Service,
            Service,
            on_registry_close=close_mock,
        )

        await registry.aclose()

        close_mock.assert_awaited_once()
        assert "tests.ifaces.Service" == caplog.records[0].svcs_service_name

    def test_contains(self, registry):
        """
        If a service is registered with a registry, `in` returns True, False
        otherwise.
        """
        registry.register_factory(Service, Service)

        assert Service in registry
        assert AnotherService not in registry


class TestRegisteredService:
    def test_repr(self, rs):
        """
        repr uses the fully-qualified name of a svc type.
        """

        assert (
            "<RegisteredService(svc_type=tests.ifaces.Service, "
            "<class 'tests.ifaces.Service'>, takes_container=False, "
            "has_ping=False"
            ")>"
        ) == repr(rs)

    def test_name(self, rs):
        """
        The name property deducts the correct class name.
        """

        assert "tests.ifaces.Service" == rs.name


def wrong_annotation(foo: svcs.Registry) -> int:
    ...


def no_args():
    ...


def diff_name():
    ...


class TestTakesContainer:
    @pytest.mark.parametrize(
        "factory",
        [no_args, diff_name, wrong_annotation],
    )
    def test_nope(self, factory):
        """
        Functions with different names and annotations are ignored.
        """
        assert not svcs._core._takes_container(factory)

    def test_name(self):
        """
        Return True if the name is `svcs_container`.
        """

        def factory(svcs_container):
            ...

        assert svcs._core._takes_container(factory)

    def test_annotation(self):
        """
        Return true if the first argument is annotated as `svcs.Container`.
        """

        def factory(foo: svcs.Container):
            ...

        assert svcs._core._takes_container(factory)

    def test_annotation_str(self):
        """
        Return true if the first argument is annotated as `svcs.Container`
        using a string.
        """

        def factory(bar: "svcs.Container"):
            ...

        assert svcs._core._takes_container(factory)

    def test_catches_invalid_sigs(self):
        """
        If the factory takes more than one parameter, raise an TypeError.
        """

        def factory(foo, bar):
            ...

        with pytest.raises(
            TypeError, match="Factories must take 0 or 1 parameters."
        ):
            svcs._core._takes_container(factory)

    def test_call_works(self):
        """
        Does not raise if the factory is a class with __call__.
        """

        class Factory:
            def __call__(self, svcs_container):
                ...

        assert svcs._core._takes_container(Factory())

    def test_signature_fails(self):
        """
        If getting the signature fails, it means the factory doesn't get a
        container.
        """
        assert not svcs._core._takes_container(int)


class TestFullName:
    def test_object(self):
        """
        Object has neither ``__module__`` nor ``__qualname__``, so it gets
        repr'ed.
        """
        assert svcs._core._full_name(object()).startswith(
            "<object object at 0x"
        )

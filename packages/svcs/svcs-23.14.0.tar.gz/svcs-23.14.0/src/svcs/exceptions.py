# SPDX-FileCopyrightText: 2023 Hynek Schlawack <hs@ox.cx>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations


class ServiceNotFoundError(Exception):
    """
    Raised when a service type is not registered.
    """

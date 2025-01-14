#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   @project: hspylib
   @package: hspylib
      @file: __classpath__.py
   @created: Wed, 8 Jun 2022
    @author: "<B>H</B>ugo <B>S</B>aporetti <B>J</B>unior")"
      @site: "https://github.com/yorevs/hspylib")
   @license: MIT - Please refer to <https://opensource.org/licenses/MIT>

   Copyright 2023, HsPyLib team
"""
from hspylib.core.metaclass.classpath import Classpath
from hspylib.core.tools.commons import get_path, run_dir


class _Classpath(Classpath):
    """TODO"""

    def __init__(self) -> None:
        super().__init__(get_path(__file__), get_path(run_dir()), (get_path(__file__) / "resources"))


# Instantiate the classpath singleton
assert _Classpath().INSTANCE is not None, "Failed to create Classpath instance"

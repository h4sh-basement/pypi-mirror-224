#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   @project: HsPyLib-Kafman
   @package: kafman.core.schema.json.property
      @file: primitive_property.py
   @created: Fri, 1 Jul 2022
    @author: "<B>H</B>ugo <B>S</B>aporetti <B>J</B>unior")"
      @site: "https://github.com/yorevs/hspylib")
   @license: MIT - Please refer to <https://opensource.org/licenses/MIT>

   Copyright 2023, HsPyLib team
"""

from kafman.core.schema.json.json_type import JsonType
from kafman.core.schema.schema_field import SchemaField
from typing import Any


class PrimitiveProperty(SchemaField):
    def __init__(self, name: str, description: str, p_type: JsonType, default: Any = None, required: bool = True):
        super().__init__(name, description, p_type, default, required)

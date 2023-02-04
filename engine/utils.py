#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-02-2023 01:01 pm
# @Author  : bhaskar.uprety
# @File    : utils.py

"""utils.py File created on 04-02-2023"""
from os import mkdir
from os.path import exists, join
from pathlib import Path as __Path
from typing import final, TypedDict

BASE_PATH: final = __Path(__file__).parent.parent.absolute()
CONFIG_DIR_PATH: final = join(BASE_PATH, 'config')

if not exists(CONFIG_DIR_PATH):
    mkdir(CONFIG_DIR_PATH)

# ========================================================================

PRIVATE_KEY_FILE_NAME: final = join(CONFIG_DIR_PATH, 'private.pem')
PUBLIC_KEY_FILE_NAME: final = join(CONFIG_DIR_PATH, 'public.pem')
CONFIG_FILE_NAME: final = join(CONFIG_DIR_PATH, 'config.json')


class Config(TypedDict):
    """Type hint for config"""
    username: str
    totp_code: str

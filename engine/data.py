#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-02-2023 01:13 pm
# @Author  : bhaskar.uprety
# @File    : data

"""data File created on 04-02-2023"""
from json import dumps, loads
from os.path import exists

from .utils import Config, PRIVATE_KEY_FILE_NAME, PUBLIC_KEY_FILE_NAME, CONFIG_FILE_NAME


def all_available():
    """Check all settings are available or not"""
    all_exist = []
    ok = exists(PRIVATE_KEY_FILE_NAME)
    all_exist.append(ok)
    ok = exists(PUBLIC_KEY_FILE_NAME)
    all_exist.append(ok)
    ok = exists(CONFIG_FILE_NAME)
    all_exist.append(ok)
    return False not in all_exist


def save_pub_key(content: str) -> None:
    """Save secret key file"""
    with open(PUBLIC_KEY_FILE_NAME, 'w') as f:
        f.write(content)


def save_prv_key(content: str) -> None:
    """Save secret key file"""
    with open(PRIVATE_KEY_FILE_NAME, 'w') as f:
        f.write(content)


def save_config(data: Config) -> None:
    """Read config file"""
    with open(CONFIG_FILE_NAME, 'w') as f:
        data = dumps(data)
        f.write(data)


def pub_key_data() -> str:
    """Read from key file"""
    with open(PUBLIC_KEY_FILE_NAME, 'r') as f:
        data = f.read()
    return data


def prv_key_data() -> str:
    """Read from key file"""
    with open(PRIVATE_KEY_FILE_NAME, 'r') as f:
        data = f.read()
    return data


def config_data() -> Config:
    """Read config file"""
    with open(CONFIG_FILE_NAME, 'r') as f:
        data = f.read()
    json_data = loads(data)
    return json_data

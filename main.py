#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 26-01-2023
# @Time    : 02:26 pm
# @Author  : JRudransh
# @File    : main.py

"""main.py File created on 26-01-2023"""
from dashboard.main import Dashboard
from engine.main import Engine

engine = Engine()
app = Dashboard()
app.close_engine = engine.close
engine.start_handler = app.start_handler
engine.message_handler = app.message_handler
engine.start()

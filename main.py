#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 26-01-2023
# @Time    : 02:26 pm
# @Author  : JRudransh
# @File    : main.py

"""main.py File created on 26-01-2023"""
from threading import Thread

from dashboard.main import Dashboard
from engine.main import Engine

engine = Engine()
app = Dashboard()
engine.start_handler = app.start_handler
engine.message_handler = app.message_handler
t = Thread(target=engine.start, daemon=True)
t.start()
app.run()

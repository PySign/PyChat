#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 26-01-2023 02:55 pm
# @Ticket  : EZB-
# @Author  : bhaskar.uprety
# @File    : user_section.py

"""user_section File created on 26-01-2023"""
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import Frame

from .utils import user_section_width


class UserSection(Frame):
    """Implemented Users Section"""

    def __init__(self, key_bind: KeyBindings):
        self.key_bind = key_bind
        title = 'ONLINE USERS'
        label = FormattedTextControl(text=title)
        self.window = Window(width=user_section_width, content=label)
        super().__init__(self.window)

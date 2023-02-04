#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 26-01-2023
# @Time    : 03:42 pm
# @Ticket  : EZB-
# @Author  : bhaskar.uprety
# @File    : screen_area.py

"""screen_area File created on 26-01-2023"""
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import Frame


class ScreenArea(Frame):
    """Implemented Users Section"""

    def __init__(self, key_bind: KeyBindings):
        self.key_bind = key_bind
        self.__screen = FormattedTextControl(text='@ Welcome message\n')
        self.__window = Window(content=self.__screen, wrap_lines=True)
        super().__init__(self.__window)

    def clear(self):
        """Clear the screen"""
        self.__screen.text = ''

    def send(self, message):
        """Display message as sent"""
        self.__screen.text += message

    def recieve(self, data: dict):
        """Display a recieved message"""
        user = data['user']
        message = data['message']
        content = f'{user}$ {message}\n'
        self.__screen.text += content

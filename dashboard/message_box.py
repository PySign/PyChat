#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 26-01-2023 02:57 pm
# @Ticket  : EZB-
# @Author  : bhaskar.uprety
# @File    : message_box.py

"""message_box File created on 26-01-2023"""

from prompt_toolkit.buffer import Buffer
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import BufferControl
from prompt_toolkit.layout.processors import BeforeInput
from prompt_toolkit.widgets import Frame

from .utils import message_box_height


class MessageBox(Frame):
    """Implemented Users Section"""

    def __init__(self, key_bind: KeyBindings):
        self.key_bind = key_bind
        self.__buffer = Buffer()
        input_box = BufferControl(buffer=self.__buffer, input_processors=[BeforeInput('$ ')])
        self.__window = Window(content=input_box, height=message_box_height, wrap_lines=True)
        self.set_key_bind()
        super().__init__(self.__window)

    @property
    def buffer(self) -> str:
        """Get all content from buffer"""
        return self.__buffer.text

    @property
    def message(self) -> str:
        """Get the message from messagebox"""
        text = self.buffer
        prefix = 'root$ '
        message = f'{prefix}{text}\n'
        self.clear()
        return message

    def clear(self):
        """Make messagebox empty"""
        self.__buffer.text = ''

    def set_key_bind(self):
        """Implemented Dashboard.set_key_bind"""
        self.key_bind.add(Keys.ControlC)(lambda _: self.clear())

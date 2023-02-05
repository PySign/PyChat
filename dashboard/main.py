#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 26-01-2023 02:50 pm
# @Ticket  : EZB-
# @Author  : bhaskar.uprety
# @File    : main.py

"""main File created on 26-01-2023"""
import json

from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.layout.containers import HSplit, VSplit
from prompt_toolkit.layout.layout import Layout

from .message_box import MessageBox
from .screen_area import ScreenArea
from .user_section import UserSection


class Dashboard(Application):
    """Implemented Dashboard"""

    def __init__(self):
        super().__init__(full_screen=True)
        self.key_bindings = KeyBindings()

        self.__user_section = UserSection(self.key_bindings)
        self.__message_box = MessageBox(self.key_bindings)
        self.__screen_area = ScreenArea(self.key_bindings)

        self.__layout = None
        self.create_layout()
        self.set_layout()
        self.set_key_bind()

        self.socket = None

    def create_layout(self):
        """Implemented Dashboard.create_layout"""
        self.__layout = VSplit(
            [
                HSplit(
                    [self.__screen_area, self.__message_box]
                ),
                self.__user_section
            ], padding=1, width=2)

    def set_layout(self):
        """Setting the dashboard layout"""
        self.layout = Layout(self.__layout)

    def process_message(self):
        """Implemented send message method"""
        buffer = self.__message_box.buffer
        if buffer:
            if '/' in buffer[0]:
                # INFO: Clear the message box
                self.__message_box.clear()
                buffer = buffer[1:]
                # INFO: Perform the operation
                if buffer in ['clear', 'cls', 'c']:
                    self.__screen_area.clear()
                elif buffer in ['exit', 'quit', 'q']:
                    self.exit()
            else:
                message = self.__message_box.message
                self.__screen_area.send(message)
                self.socket.send(buffer)

    def set_key_bind(self):
        """Implemented Dashboard.set_key_bind"""
        self.key_bindings.add(Keys.Enter)(lambda _: self.process_message())
        self.key_bindings.add(Keys.ControlQ)(lambda event: event.app.exit())

    def message_handler(self, _, message):
        """Implemented message_handler in Dashboard"""
        message = json.loads(message)
        if message['topic'] == 'msg':
            self.__screen_area.recieve(message)

    def start_handler(self, socket):
        """Implemented start_handler in Dashboard"""
        self.socket = socket

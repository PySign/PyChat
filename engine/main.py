#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-02-2023 12:55 pm
# @Author  : bhaskar.uprety
# @File    : main.py

"""main File created on 04-02-2023"""

from requests import post
from websocket import WebSocketApp

from .data import all_available, config_data, save_config, save_prv_key, save_pub_key
from .security import generate_keypair, get_totp


class Engine:
    """Implemented Engine"""

    def __init__(self, url="ws://localhost:8000/chat"):
        self.username: str = ''
        self.totp_code: str = ''
        self.headers = {}
        self.url = url

        self.ws = None
        self.ws: WebSocketApp
        self.message_handler = None
        self.start_handler = None

        if not all_available():
            self.signup()
        self.get_data()

    @staticmethod
    def signup():
        """Implemented signup in Engine"""
        public, private = generate_keypair()
        save_pub_key(public)
        save_prv_key(private)
        username = input('Enter Username: ')
        data = {
            'username': username,
            'public_key': public
        }
        res = post('http://127.0.0.1:8000/user', json=data)
        data = res.json()
        save_config(data)

    def get_data(self):
        """Implemented get_data in Engine"""
        data = config_data()
        self.username = data['username']
        self.headers['username'] = self.username
        totp = get_totp()
        self.headers['token'] = totp

    def create_connection(self):
        """Implemented create_connection in Engine"""
        if self.message_handler and self.start_handler:
            self.ws = WebSocketApp(
                self.url, header=self.headers,
                on_message=self.message_handler,
                on_open=self.start_handler
            )
        else:
            raise Exception('Set all handlers first')

    def start(self):
        """Implemented start in Engine"""
        self.create_connection()
        self.ws.run_forever()

    def close(self):
        """Implemented close in Engine"""
        self.ws.close()

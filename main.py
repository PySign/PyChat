#!/usr/bin/env python

from prompt_toolkit import Application, styles
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window, HSplit
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.processors import BeforeInput
from prompt_toolkit.formatted_text import HTML
# from prompt_toolkit.application import get_app


buffer1 = Buffer()  # Editable buffer.

# Windows
# 1. Sidebar
sidebar = FormattedTextControl(text='ONLINE USERS\n')
sidebar_width = 30

# 2. Message box
msg_input = BufferControl(buffer=buffer1, input_processors=[
    BeforeInput('$ ')
])
msg_height = 2

# Root container
msg_box = FormattedTextControl(text='Welcome message')

root_container = VSplit(
    [
        HSplit(
            [
                Window(content=msg_box),
                Window(content=msg_input, height=msg_height)
            ], padding=1, padding_char='*',
        ),
        Window(content=sidebar, width=sidebar_width),
    ], padding=1, width=2)

layout = Layout(root_container)


def format_message(text):
    prefix = '\n$ '
    text = f'{prefix}{text}'
    return text


def send_message():
    text = buffer1.text
    formatted = format_message(text)
    msg_box.text += formatted
    # get_app().invalidate()
    buffer1.text = ''


def bottom_toolbar():
    return HTML('This is a <b><style bg="ansired">Toolbar</style></b>!')


kb = KeyBindings()


@kb.add('c-c')
def _clear(event):
    msg_box.text = ''


@kb.add('c-q')
def exit_(event):
    """
    Pressing Ctrl-Q will exit the user interface.

    Setting a return value means: quit the event loop that drives the user
    interface and return this value from the `Application.run()` call.
    """
    event.app.exit()


@kb.add('enter')
def send(event):
    send_message()


app = Application(layout=layout, full_screen=True, key_bindings=kb)
app.run()

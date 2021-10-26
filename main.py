#!/usr/bin/env python

from prompt_toolkit import Application, prompt, styles
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window, HSplit
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.processors import BeforeInput

style = styles.Style.from_dict({
        'color': "#ffffff",
        'bgcolor': '#ff0000',
})

buffer1 = Buffer()  # Editable buffer.

# Windows
# 1. Sidebar
sidebar = FormattedTextControl(text='Hello world')
sidebar_width = 30

# 2. Message box
msg_input = BufferControl(buffer=buffer1, input_processors=[
    BeforeInput('$ ')
])
msg_height = 2

root_container = VSplit(
    [
        HSplit(
            [
                Window(content=FormattedTextControl(text='Hello world')),
                Window(content=msg_input, height=msg_height)
            ], padding=1, padding_char='*',
        ),
        Window(content=sidebar, width=sidebar_width),
    ], padding=1, width=2)

layout = Layout(root_container)

kb = KeyBindings()


@kb.add('c-q')
def exit_(event):
    """
    Pressing Ctrl-Q will exit the user interface.

    Setting a return value means: quit the event loop that drives the user
    interface and return this value from the `Application.run()` call.
    """
    event.app.exit()


app = Application(layout=layout, full_screen=True, key_bindings=kb)
app.run()

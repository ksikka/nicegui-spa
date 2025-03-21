#!/usr/bin/env python3
import tab_one
from tabmanager import TabManager

from nicegui import ui

import logging
logging.basicConfig(level=logging.DEBUG)

@ui.page('/')  # normal index page (e.g. the entry point of the app)
@ui.page('/{_:path}')  # all other pages will be handled by the router but must be registered to also show the SPA index page
def main():
    tab_manager = TabManager()
    tab_manager.add_tab("/", tab_one.TabOne("/two"))
    tab_manager.add_tab("/two", tab_one.TabOne("/"))

    # adding some navigation buttons to switch between the different pages
    with ui.row():
        ui.button('One', on_click=lambda: tab_manager.switch_tab("/")).classes('w-32')
        ui.button('Two', on_click=lambda: tab_manager.switch_tab("/two")).classes('w-32')

    # this places the content which should be displayed
    tab_manager.build()


ui.run(host='0.0.0.0', uvicorn_logging_level=logging.DEBUG)

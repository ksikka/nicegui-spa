#!/usr/bin/env python3
import tab_one
from router import Router

from nicegui import ui

import logging
logging.basicConfig(level=logging.DEBUG)

@ui.page('/')  # normal index page (e.g. the entry point of the app)
@ui.page('/{_:path}')  # all other pages will be handled by the router but must be registered to also show the SPA index page
def main():
    router = Router()
    router.add_route("/", tab_one.TabOne())

    @router.add('/two')
    def show_two():
        ui.label('Content Two').classes('text-2xl')

    @router.add('/three')
    def show_three():
        ui.label('Content Three').classes('text-2xl')

    # adding some navigation buttons to switch between the different pages
    with ui.row():
        ui.button('One', on_click=lambda: router.open("/")).classes('w-32')
        ui.button('Two', on_click=lambda: router.open(show_two)).classes('w-32')
        ui.button('Three', on_click=lambda: router.open(show_three)).classes('w-32')

    # this places the content which should be displayed
    router.frame().classes('w-full p-4 bg-gray-100')


ui.run(host='0.0.0.0', uvicorn_logging_level=logging.DEBUG)

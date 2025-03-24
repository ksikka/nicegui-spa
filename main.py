#!/usr/bin/env python3
import tab_one
from tabmanager import TabManager
import tabs

from nicegui import ui

import logging

logging.basicConfig(level=logging.DEBUG)


# Root and all pages will return the "single-page-app".
# All pages are prefixed by /p/ to allow for other routes to
# co-exist, such as /_nicegui/auto routes needed when using ui.image.
@ui.page("/")
@ui.page("/p/{path}")
def main():
    tab_manager = TabManager()
    tab_manager.add_tab("/p/home", tabs.home.Home())

    # adding some navigation buttons to switch between the different pages
    with ui.header():
        # ui.image("img/LightningPose_horizontal_light.webp")
        # replace= removes the default .nicegui-link which made the link blue and underlined.
        ui.link("Home", "/p/home").classes(replace="text-lg text-white soft-link")

    # this places the content which should be displayed
    tab_manager.build()


ui.run(
    host="0.0.0.0",
    uvicorn_logging_level=logging.DEBUG,
    prod_js=False,
    title="Lightning Pose",
    favicon="img/favicon.ico",
)

#!/usr/bin/env python3
import os

# Override storage path before importing nicegui.
os.environ["NICEGUI_STORAGE_PATH"] = os.path.expanduser("~/.lightning-pose")

import logging

from nicegui import ui

import tab_one
import tabs
from tabmanager import TabManager




# Root and all pages will return the "single-page-app".
# All pages are prefixed by /p/ to allow for other routes to
# co-exist, such as /_nicegui/auto routes needed when using ui.image.
@ui.page("/")
@ui.page("/p/{path}")
def main():
    tab_manager = TabManager()
    tab_manager.add_tab("/p/home", tabs.home.Home())
    tab_manager.add_tab("/p/models", tabs.models.Models())
    tab_manager.add_tab("/p/faketab", tab_one.TabOne("/p/models"))

    # adding some navigation buttons to switch between the different pages
    with ui.header():
        # ui.image("img/LightningPose_horizontal_light.webp")
        # replace= removes the default .nicegui-link which made the link blue and underlined.
        ui.link("Home", "/p/home").classes(replace="text-lg text-white soft-link")
        ui.link("Models", "/p/models").classes(replace="text-lg text-white soft-link")
        ui.link("TestTab", "/p/faketab").classes(replace="text-lg text-white soft-link")

    # this places the content which should be displayed
    tab_manager.build()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        host="0.0.0.0",
        #uvicorn_logging_level=logging.DEBUG,
        prod_js=False,
        title="Lightning Pose",
        favicon="img/favicon.ico",
    )

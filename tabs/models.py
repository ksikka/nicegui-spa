import asyncio
import enum

import config
from dao.model import Model
from nicegui import ui, background_tasks


class LoadingState(enum.Enum):
    LOADING = 1
    COMPLETED = 2
    FAILED = 3

class Models:
    def __init__(self) -> None:
        self.model_loading_state = LoadingState.LOADING
        self.models = []
        background_tasks.create(self.load_models())

    # Asynchronously load models from filesystem.
    async def load_models(self):
        self.models = await Model.async_list()
        self.model_loading_state = LoadingState.COMPLETED
        self.build.refresh()


    async def train_model(self):
        await asyncio.sleep(1)
        self.models = [
            {'name': 'Alice', 'created': 18},
            {'name': 'Bob', 'created': 21},
            {'name': 'Carol'},
        ]
        self.build.refresh()


    @ui.refreshable
    def build(self):
        if self.model_loading_state == LoadingState.LOADING:
            ui.label("Loading...")
        if self.model_loading_state == LoadingState.COMPLETED:
            if len(self.models) == 0:
                ui.label(f"No models found in {config.model_dir}.")
                ui.button("New model", on_click=self.train_model)
            else:
                ui.button("New model", on_click=self.train_model)

                columns = [
                    {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left', 'sortable': True},
                    {'name': 'created', 'label': 'Created', 'field': 'creation_timestamp_fmt', 'sortable': True},
                ]

                ui.table(columns=columns, rows=self.models, row_key='name')


import asyncio

from nicegui import ui


class ModelsEmptyState:
    def build(self):
        "you have no models, want to train a model?"
        pass


class ModelsList:
    def build(self):
        pass


class Models:
    def __init__(self) -> None:
        pass

    def build(self):
        # Empty state
        pass

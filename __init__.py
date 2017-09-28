"""
Clock
"""
import asyncio
from pyplanet.apps.config import AppConfig
from .views import ClockWidget

class Clock(AppConfig):
    game_dependencies = ['trackmania','shootmania']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = ClockWidget(self)

    async def on_start(self):
        await self.widget.display()

    async def player_connect(self):
        await self.widget.display()

    async def map_start(self, *args,**kwargs):
        await self.widget.display()
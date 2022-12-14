
import asyncio
from dotenv import load_dotenv
import os

from client import ModularClient
from modules.mock import Mock
from modules.summon import Summon
from modules.copypasta import CopyPasta
from modules.edit_shame import EditShame
from services.console import Console


async def main():
    load_dotenv() # Does nothing if it can't find .env
    DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    BUILD = os.getenv('BUILD')

    client = ModularClient()

    client.add_module(Mock())
    client.add_module(Summon())
    client.add_module(CopyPasta("resources/copypasta.json"))
    client.add_module(EditShame())

    if BUILD == 'DEVELOPMENT':
        client.add_service(Console())

    print('Attempting to Connect to Discord')
    await client.start(DISCORD_BOT_TOKEN)


if __name__ == '__main__':
    asyncio.run(main())

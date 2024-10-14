from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot:
    def __init__(self):
        self.one = Client(
            name="aliceAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="aliceAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="aliceAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="aliceAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="aliceAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")

        async def start_assistant(client, name, index):
            if getattr(config, f'STRING{index}'):
                await client.start()
                try:
                    await client.join_chat("thanosprosss")
                    await client.join_chat("learning_bots")
                except Exception as e:
                    LOGGER(__name__).error(f"Assistant {name} failed to join chats: {e}")
                
                assistants.append(index)
                try:
                    await client.send_message(config.LOG_GROUP_ID, f"Assistant {name} Started")
                except Exception:
                    LOGGER(__name__).error(
                        f"Assistant Account {index} has failed to access the log Group. "
                        "Make sure that you have added your assistant to your log group and promoted it as admin!"
                    )
                    raise SystemExit

                client.id = client.me.id if client.me else None
                client.name = client.me.mention if client.me else None
                client.username = client.me.username if client.me else None
                assistantids.append(client.id)
                LOGGER(__name__).info(f"Assistant {name} Started as {client.name}")

        # Start each assistant if its session string is defined
        await start_assistant(self.one, "One", 1)
        await start_assistant(self.two, "Two", 2)
        await start_assistant(self.three, "Three", 3)
        await start_assistant(self.four, "Four", 4)
        await start_assistant(self.five, "Five", 5)

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except Exception as e:
            LOGGER(__name__).error(f"Error stopping assistants: {e}")

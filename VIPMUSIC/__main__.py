
import asyncio
import importlib
from pyrogram import idle
import config
from config import BANNED_USERS
from VIPMUSIC import HELPABLE, LOGGER, app, userbot
from VIPMUSIC.core.call import VIP
from VIPMUSIC.plugins import ALL_MODULES
from VIPMUSIC.utils.database import get_banned_users, get_gbanned
from telethon import TelegramClient
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import threading

# Application Builder
app_builder = ApplicationBuilder().token(config.BOT_TOKEN)

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("VIPMUSIC").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return

    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        LOGGER("VIPMUSIC").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    await app.start()

    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(all_module)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
            LOGGER("VIPMUSIC.plugins").info("Successfully Imported All Modules ")

    await userbot.start()
    await VIP.start()
    await VIP.decorators()

    # Start hina in a new thread
    def start_hina():
        hina = app_builder.build()
        hina.run_polling()

    threading.Thread(target=start_hina).start()

    LOGGER("VIPMUSIC").info("VIPMUSIC STARTED SUCCESSFULLY 🕊️")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop_policy().get_event_loop().run_until_complete(init())
    LOGGER("VIPMUSIC").info("Stopping VIPMUSIC! GoodBye")
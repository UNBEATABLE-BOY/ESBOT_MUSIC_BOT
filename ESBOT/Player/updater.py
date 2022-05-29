


import os
import sys

from os import system, execle, environ

from pyrogram.types import Message
from pyrogram import filters
from ESBOT.main import bot as Client

from config import UPSTREAM_REPO, BOT_USERNAME

from ESBOT.filters import command
from ESBOT.decorators import sudo_users_only




@Client.on_message(command(["restart", f"restart@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply_text("❖ Restarting bot...")
        print("[INFO]: BOT SERVER RESTARTED !!")
    except BaseException as err:
        print(f"[ERROR]: {err}")
        return
    await msg.edit_text("✅ Bot has restarted !\n\n» back active again in 5-10 seconds.")
    os.system(f"kill -9 {os.getpid()} && python3 main.py")

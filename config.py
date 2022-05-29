## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Umk")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "SHRAAJ")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ESBOT_ASSISTANT")
ALIVE_NAME = getenv("ALIVE_NAME", "SHRAAJ")
BOT_USERNAME = getenv("BOT_USERNAME", "ESBOT_MUSIC2_BOT")
OWNER_ID = getenv("OWNER_ID", "1669178360")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ESBOT_ASSISTANT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ESBOT_HELP")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LIFE_CODES")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "213812213").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/9cd5d21c87d87f2332927.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/e3798e18ba07accc0faea.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "500"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ESBOT/ESBOT-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/76959b7ea876e072d2d60.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/ccaf138a0c76bbde52ad8.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/723b29703d015df34236c.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/ccaf138a0c76bbde52ad8.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/e3798e18ba07accc0faea.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/3ab0ac001a6ad823cb094.jpg")

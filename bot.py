

import os
import logging
from config import Config
from pyrogram import Client as Clinton
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

if __name__ == "__main__" :
    # DEBUG LINES: Add these two lines
    print(f"DEBUG: Using API_ID: {Config.API_ID}")
    print(f"DEBUG: Using API_HASH: {Config.API_HASH}")

    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

        Warrior = Clinton(
        "@BOT_X_BOT",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=30,  # Add this line
        plugins=plugins
        )

    
    

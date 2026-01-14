

import os
import logging
from config import Config
from pyrogram import Client as Clinton
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

if __name__ == "__main__" :
    import time # Add this at the top or here
    # 1. Create directory first
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    # 2. DEFINE THE PLUGINS VARIABLE (This was the missing part)
    plugins = dict(root="plugins")

    # 3. Now you can use 'plugins' in the client initialization
    Warrior = Clinton(
        "@BOT_X_BOT",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=60, # Increased threshold
        workers=20,
        plugins=plugins
    )
    print("Starting bot... waiting 5 seconds for time sync.")
    time.sleep(5) 
    Warrior.run()
    
    
    

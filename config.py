import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    # The Telegram API things
    raw_api_id = os.environ.get("API_ID", "22299340")
    API_ID = int(raw_api_id) if raw_api_id and raw_api_id.strip() else 22299340

        # Find this line in your config.py and change it to this:
    raw_api_hash = os.environ.get("API_HASH", "09b09f3e2ff1306da4a19888f614d937")
    API_HASH = raw_api_hash if raw_api_hash and raw_api_hash.strip() else "09b09f3e2ff1306da4a19888f614d937"
    
    #API_HASH = os.environ.get("API_HASH", "09b09f3e2ff1306da4a19888f614d937")
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4194304000 #2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    # your telegram id
    raw_owner_id = os.environ.get("OWNER_ID", "5380609667")
    OWNER_ID = int(raw_owner_id) if raw_owner_id and raw_owner_id.strip() else 5380609667
    
    SESSION_NAME = "UPLOADER-X-BOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://mikota4432:jkJDQuZH6o8pxxZe@cluster0.2vngilq.mongodb.net/?retryWrites=true&w=majority")
    MAX_RESULTS = "50"
    PREMIUM_USER = os.environ.get("PREMIUM_USER", "5380609667")

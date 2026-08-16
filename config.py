import os

API_ID = int(os.environ.get("API_ID", "23621595"))
API_HASH = os.environ.get("API_HASH", "de904be2b4cd4efe2ea728ded17ca77d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://newmongo3_db_user:newmongo3_db_user@cluster0.v1ajjjc.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "SilentXBotz")

WEB_SERVER = os.environ.get("WEB_SERVER", "True").lower() in ("true", "1", "t")
PORT = int(os.environ.get("PORT", "8080"))
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))

TG_WORKERS = int(os.environ.get("TG_WORKERS", "4"))

# Your Koyeb/Heroku App Url
# Example : https://yorappurl.koyeb.app/
APP_URL = os.environ.get("APP_URL", https://slippery-janna-newbot099-1b0d2cc4.koyeb.app/)

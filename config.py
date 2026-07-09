import os


BOT_TOKEN = os.getenv("BOT_TOKEN")

CHAT_ID = os.getenv("CHAT_ID")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


if not BOT_TOKEN:
    raise Exception("BOT_TOKEN missing")


if not CHAT_ID:
    raise Exception("CHAT_ID missing")


if not GEMINI_API_KEY:
    raise Exception("GEMINI_API_KEY missing")

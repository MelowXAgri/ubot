from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", "28155542"))

API_HASH = getenv("API_HASH", "6aa43200e5640303c03d99b8e5d3dd8a")

BOT_TOKEN = getenv("BOT_TOKEN", "5662215015:AAGPyGaAbKYFZB0CJPPUHvVSFmExBtZ4uSg")

OWNER_ID = int(getenv("OWNER_ID", "6288681216"))

LOGS_MAKER_UBOT = int(getenv("LOGS_MAKER_UBOT", "-1002106247790"))

MAX_BOT = int(getenv("MAX_BOT", "25"))

RMBG_API = getenv("RMBG_API", "b5ZnjZ2nUUpbdEHfcrWdjWbC")

OPENAI_KEY = getenv("OPENAI_KEY", "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")

MONGO_URL = getenv("MONGO_URL", "mongodb+srv://suker:suker@cluster0.qlhzhe1.mongodb.net/?retryWrites=true&w=majority")

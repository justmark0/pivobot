import logging
import os
from pathlib import Path

from aiogram import Bot
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

APP_BASE_DIR = Path(__file__).resolve().parent.parent

TARGET_CHAT_ID = os.getenv("TARGET_CHAT_ID")

stickers = {
    1: r'CAACAgIAAxkBAAEFZ2ti4u1rxrpWv5E2UG9o19Xjy1I4NwACxBgAAkMQAUvmQ9pgKTsgpCkE',
    2: r'CAACAgIAAxkBAAEFZ21i4u2yMV-98_AGJh0_H0YS_Q3wcQAC9xcAAiN0AAFLGTbEN8h52i8pBA',
    3: r'CAACAgIAAxkBAAEFZ29i4u20nvo9XJjvx2aqGWTcthKS7AACUhsAAs3XAAFLseMDylER2BwpBA',
    4: r'CAACAgIAAxkBAAEFZ3Fi4u22Sg3aLnmOGCCRp_gGko5RjAACjBMAAthuCUu5Cw6-umiwuCkE',
    5: r'CAACAgIAAxkBAAEFZ3Ni4u24HpPAb2CSoBy8qzsQa8AnbgAChxcAAuB4AUtjbsHL1NpbdSkE',
    6: r'CAACAgIAAxkBAAEFZ3Vi4u25DSLwJePNQFAMtGlSJAqAfAAC3hgAAiEkAUubZrQCbS753ykE',
    7: r'CAACAgIAAxkBAAEFZ3di4u27pb6mPye92FtScgaGdYTOGwACjRcAAgoiAAFLJIWgnm3S4vcpBA',
}

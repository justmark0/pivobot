import asyncio
import datetime
import time

from config import TARGET_CHAT_ID, bot, stickers


async def send_sticker():
    weekday = datetime.datetime.today().weekday() + 1
    await bot.send_sticker(TARGET_CHAT_ID, sticker=stickers[weekday])
    print(f'Sent {weekday} sticker at {datetime.datetime.now()}')


def should_send_message(dt) -> bool:
    today = datetime.datetime.today().date()
    if not dt or today > dt:
        return True
    return False


if __name__ == "__main__":
    dt_last_sticker_send = None

    while True:
        if should_send_message(dt_last_sticker_send):
            asyncio.run(send_sticker())
            dt_last_sticker_send = datetime.datetime.today().date()

        time.sleep(10)

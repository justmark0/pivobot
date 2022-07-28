import asyncio
import datetime
import pytz
import time

from config import TARGET_CHAT_ID, bot, stickers


async def send_sticker():
    weekday = datetime.datetime.today().weekday() + 1
    await bot.send_sticker(TARGET_CHAT_ID, sticker=stickers[weekday])
    now = datetime.datetime.now(tz=pytz.timezone('Europe/Moscow'))
    print(f'Sent {weekday} sticker at {now}')


def should_send_message(dt) -> bool:
    today = datetime.datetime.now(tz=pytz.timezone('Europe/Moscow')).date()
    if not dt:
        print(f'Today is {today}')
    if not dt or today > dt:
        return True
    return False


if __name__ == "__main__":
    dt_last_sticker_send = None

    while True:
        if should_send_message(dt_last_sticker_send):
            asyncio.run(send_sticker())
            dt_last_sticker_send = datetime.datetime.now(tz=pytz.timezone('Europe/Moscow')).date()

        time.sleep(10)

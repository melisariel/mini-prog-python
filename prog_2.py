from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
import time, random, os

api_id = # ID аккаунта
api_hash = 'Hash аккаунта'

client = TelegramClient('session_name', api_id, api_hash)

recipient = 'Юзернейм пользователя'
message = 'Сообщение'
max_repeats = 50
delay_between = 1

with client:
    for i in range(max_repeats):
        try:
            client.send_message(recipient, message)
            print(f'Отправлено {i+1}/{max_repeats}')
        except FloodWaitError as e:
            print(f'Жду {e.seconds}s')
            time.sleep(e.seconds + 5)
        except Exception as e:
            print(f'Ошибка: {e}')
            break
        time.sleep(delay_between + random.uniform(0, 3))

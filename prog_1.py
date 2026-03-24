from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
import time
import os

api_id = # ID аккаунта
api_hash = 'Hash аккаунта'

client = TelegramClient('daily_multiple', api_id, api_hash)

message = (
    "Текст сообщения"
)

common_image_path = ''

user_images = {

}

delay_between = 10

with client:
    for user, individual_image_path in user_images.items():
        try:
            if not os.path.isfile(common_image_path):
                print(f'Общий файл не найден: {common_image_path}')
                continue
            if not os.path.isfile(individual_image_path):
                print(f'Индивидуальный файл для {user} не найден: {individual_image_path}')
                continue

            client.send_message(user, message)

            client.send_file(user, common_image_path, caption="Закреп")

            client.send_file(user, individual_image_path, caption="Подписка")

            print(f'Успешно отправлено {user}')

        except FloodWaitError as e:
            print(f'Telegram ограничил: жду {e.seconds} секунд...')
            time.sleep(e.seconds)
        except Exception as e:
            print(f'Ошибка при отправке {user}: {e}')

        time.sleep(delay_between)

from pyrogram import Client
import shelve
import random
import time

api_id = 8228878
api_hash = "8a948f28b11e4146c9e233aa2b2f121d"
phone_number = '+79630616024'
PUBLIC = ["chop_choop","mudak","OAOAOMMM"]

TEXTS = [
    '.',
    '/',
    '.ь',
]

COMMENT_EVERY_N = 1  # комментируем каждое N собщение
                     # если равно 1, комментируем каждое сообщение
                     # если равно 3, комментируем каждое третье
                     # если равно 5, комментируем каждое пятое ... итд

processed_message = shelve.open('processed_message.db', writeback=True)

# создаем клиент телеграма
app = Client("chelik", api_id, api_hash,
             phone_number=phone_number)

count = 0
 
with app:
 
    while True:
        for i in range(len(PUBLIC)):
            public = app.get_chat(PUBLIC[i])  # ищем паблик по нику
            chat = public.linked_chat  # связанный чат обсуждений паблика
            for msg in app.get_history(chat.id, limit=100):
                # фильтруем только авторепосты из паблика
                if (msg.from_user is None  # если сообщение не имеет автора
                        # и это репост из паблика (проверка по id)
                        and msg.forward_from_chat.id == public.id):
                    if msg.forward_from_message_id % COMMENT_EVERY_N != 0:
                        print(f'Пропускаем message_id={msg.message_id},'
                            f' так как комментируе каждое {COMMENT_EVERY_N}')
                        continue
                    # проверяем, есть ли в списке обработанных сообщений этот айди
                    # чтобы не комментировать по несколько раз один пост
                    if str(msg.forward_from_message_id) in processed_message:
                        print(f'Пропускаем уже обработанное message_id={msg.message_id}')
                        continue
                    # пишем в список обработанных айди этого сообщения
                    processed_message[str(msg.forward_from_message_id)] = True
    
                    print(f'Обработка message_id={msg.message_id}')
    
                    text = random.choice(TEXTS)  # выбираем случайный текст из списка
                    app.send_message(chat.id, text,  # отправляем текст в чат
                                    reply_to_message_id=msg.message_id)  # как ответ на сообщение с постом
                    print(f'Текст {msg.message_id} отправлен в группу {PUBLIC[i]}')
                    break
                    # для того, чтоб не оставлять больше одного коммента за 5 минут
                    #break  # выходим из перебора сообщений, если оставили коммент
    
            print('Ставим на паузу')
            time.sleep(60*5)
from pyrogram import Client
import shelve
import random
import time

api_id = 8228878
api_hash = "8a948f28b11e4146c9e233aa2b2f121d"
phone_number = '+79630616024'
#PUBLIC = ["krasnodar_groupp", "MWchat21", 
 #       "crolchatis","CHAT_3HAKOMCTBA_24_7","CHAT_3HAKOMCTBA_16",
#        "CHAT_ACQUAINTANCES"]

print("Введите путь до txt файла с чатами")
dir = input()

with open(dir) as file:
    PUBLIC =  [row.strip() for row in file]

TEXT = ["Всем приветик😊",
        "🍑🍑🍑",
        "👉👌💦💦😅",
        "Кто пошлый + в чат😅🙈",
        "Вы классные 💕",
        "🔞",
        "🙄👉🕐💬",
        "Вы, солнышки🙊😇",
        "💋💖",
        "😀","😃","😄","😁","😆","😋","😘",
        "🙂","😧","😏","🤩","😎","🤔","🤭",
        "😶","😦","😵","😢","🙃","😇","😝",
        "😋","💑","👙","👗","👘","🔥","💥",
        "☄️","🌈","🌪","💧","💦","💨","⛄️",
        "🍏","🍎","🍑","🍒","🍑","🍍","🌠",
        "❤️","💛","💚","💙","💜","🖤","❣️",
        "💕","💞","💗","💖","💘","💝","💟","⛔️","🔞"]


app = Client("chelik", api_id, api_hash,
             phone_number=phone_number)
while True:
    with app:
        for i  in range(len(PUBLIC)):
            public = app.get_chat(PUBLIC[i])
            chat = public
            text = random.choice(TEXT)
            app.send_message(chat.id, text)
            print(f"Сообщение в чат {PUBLIC[i]} отправлено\nУхожу в откат на 5 минут")
            time.sleep(60*5)
        print("Работа по всем чатам выполнена ухожу в слип на 3 часа")
        time.sleep(60*180)

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
with app:
    
    while True:
        for i  in range(len(PUBLIC)):
            try:
                public = app.get_chat(PUBLIC[i])
                chat = public
                text = random.choice(TEXT)
                app.send_message(chat.id, text)
                print(f"Сообщение {text} отправлено в чат {PUBLIC[i]}\nУхожу в откат на 5 минут")
                time.sleep(300)
            except:
                print(f"Исключение KeyError. Не смог найти чат {PUBLIC[i]}\n")
            else:
                print("Успех! Ошибок не возникло!")
            
        print("Работа по всем чатам выполнена ухожу в слип на 1 часа")
        time.sleep(3600)

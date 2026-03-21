import os
import telebot
from flask import Flask, request

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN, threaded=False) if TOKEN else None
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_command(message):
    markup = telebot.types.InlineKeyboardMarkup()
    # Ссылка на твой домен
    my_app_url = "https://intospark-weather-bot.vercel.app/index.html" 
    # Ссылка на само приложение внутри ТГ (создается в BotFather)
    direct_link = "https://t.me/IntosparkWeatherBot/app" 
    
    btn = telebot.types.InlineKeyboardButton(
        text="Открыть Weather Pro ☁️", 
        web_app=telebot.types.WebAppInfo(url=my_app_url)
    )
    markup.add(btn)

    photo_url = f"{my_app_url}/banner.png" 

    caption_text = (
        f"<b>Intospark Weather — Погода в новом измерении</b> ☁️\n\n"
        f"🙌 Исследуйте метеоусловия через уникальный интерфейс:\n\n"
        f"1️⃣ <b><a href='{direct_link}'>Откройте приложение</a></b>\n"
        f"2️⃣ <b>Узнайте прогноз</b> для своего города с точностью до часа\n"
        f"3️⃣ <b>Наслаждайтесь эстетикой</b> — дизайн меняется вместе с погодой\n\n"
        f"Есть вопросы? Пишите в поддержку: @твой_ник 👨🏻‍💻"
    )

    try:
        bot.send_photo(message.chat.id, photo=photo_url, caption=caption_text, reply_markup=markup, parse_mode='HTML')
    except:
        bot.send_message(message.chat.id, caption_text, reply_markup=markup, parse_mode='HTML')

@app.route('/api', methods=['POST'])
def webhook():
    if bot and request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    return 'OK', 200

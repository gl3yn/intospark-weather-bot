import os
import telebot
from flask import Flask, request

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN, threaded=False) if TOKEN else None
app = Flask(__name__)

# --- ВОТ ЭТОГО БЛОКА НЕ ХВАТАЛО ---
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = telebot.types.InlineKeyboardMarkup()
    # Ссылка на твой дизайн (главная страница Vercel)
    my_app_url = "https://intospark-weather-bot.vercel.app/index.html" 
    
    btn = telebot.types.InlineKeyboardButton(
        text="Открыть Weather Pro ☁️", 
        web_app=telebot.types.WebAppInfo(url=my_app_url)
    )
    markup.add(btn)
    
    bot.reply_to(message, f"Привет, {message.from_user.first_name}! ✨\nНажми н а кнопку ниже, чтобы запустить приложение.", reply_markup=markup)
# ---------------------------------

@app.route('/api', methods=['POST'])
def webhook():
    if bot and request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    return 'OK', 200

    @bot.message_handler(commands=['start'])
def start_command(message):
    markup = telebot.types.InlineKeyboardMarkup()
    my_app_url = "https://intospark-weather-bot.vercel.app/index.html" 
    
    btn = telebot.types.InlineKeyboardButton(
        text="Открыть Weather Pro ☁️", 
        web_app=telebot.types.WebAppInfo(url=my_app_url)
    )
    markup.add(btn)

    photo_url = "https://intospark-weather-bot.vercel.app/banner.png" 

    # Текст из Варианта 1
    caption_text = (
        f"<b>Intospark Weather — Погода в прямо в Telegram</b> ☁️\n\n"
        f"1️⃣ <b><a href='https://t.me/intospark_bot/weather'>Откройте приложение</a></b>\n" # Пример ссылки        f"2️⃣ <b>Узнайте прогноз</b> для своего города с точностью до часа\n"
        f"3️⃣ <b>Наслаждайтесь эстетикой</b> — дизайн меняется вместе с погодой\n\n"
        f"Есть вопросы? Пишите в поддержку: @твой_ник 👨🏻‍💻"
    )

    bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption=caption_text,
        reply_markup=markup,
        parse_mode='HTML' # Обязательно, чтобы работали жирный шрифт <b>
    )

    @bot.message_handler(commands=['start'])
def start_command(message):
    markup = telebot.types.InlineKeyboardMarkup()
    my_app_url = "https://intospark-weather-bot.vercel.app" 
    
    btn = telebot.types.InlineKeyboardButton(
        text="Открыть Weather Pro ☁️", 
        web_app=telebot.types.WebAppInfo(url=my_app_url)
    )
    markup.add(btn)

    # Ссылка на твое изображение (лучше использовать прямую ссылку на картинку в интернете)
    # Например, можешь загрузить её на Imgur или взять из папки public своего Vercel
    photo_url = "https://intospark-weather-bot.vercel.app/banner.png" 

    bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption=f"Привет, {message.from_user.first_name}! ✨\n\nДобро пожаловать в метео-станцию будущего. Нажми на кнопку ниже, чтобы запустить приложение.",
        reply_markup=markup,
        parse_mode='HTML'
    )

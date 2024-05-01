import logging
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler, Updater

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def parse_weather():
    url = "https://yandex.kz/pogoda/almaty?lat=43.273564&lon=76.914851"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find("div", class_="link__condition day-anchor i-bem").text.strip()
    weather = soup.find("div", class_="temp fact__temp fact__temp_size_s").text.strip()
    return f"Погода сейчас в Алматы: {weather}, {container}"


def parse_weather_ten_days():
    url = "https://yandex.kz/pogoda/almaty?lat=43.273564&lon=76.914851"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    containers = soup.find("div", class_="forecast-briefly__days").text.strip()

    matches = re.findall(r'(\d+\s\w+)\+(\d+)\+(\d+)', containers)

    for match in matches[:10]:
        return f"{match[0]} днем: {match[1]}, ночью: {match[2]}"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    list1 = ["Погода сейчас в Алматы", "Погода на 10 дней в Алматы"]
    keyboard = []
    for i in list1:
        new_button = [InlineKeyboardButton(i, callback_data=i)]
        keyboard.append(new_button)

    reply_markup = InlineKeyboardMarkup(keyboard)
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=parse_weather())
    await update.message.reply_text("Выберите Действие: ", reply_markup=reply_markup)


async def button(update, context):
    query = update.callback_query
    await query.answer()
    if query.data == "Погода сейчас в Алматы":
        message = parse_weather()
    elif query.data == "Погода на 10 дней в Алматы":
        message = parse_weather_ten_days()
    await query.edit_message_text(text=message)

if __name__ == '__main__':
    application = ApplicationBuilder().token('7021129537:AAHnm5XFjtHrrCbcf_NYThUnVFK0NukeJOM').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

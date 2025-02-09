# bot.py
import os
import requests
import uuid
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from storage import activity_storage  # Импортируем локальное хранилище

# Настройки
GITHUB_API_URL = "https://api.github.com/users/{}/events"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # Убедитесь, что вы установили переменную окружения
WEB_APP_URL = "https://neomlet.github.io/"  # Замените на ваш URL

# Функция для получения активности пользователя на GitHub
def get_github_activity(username):
    response = requests.get(GITHUB_API_URL.format(username))
    if response.status_code == 200:
        return response.json()
    return None

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.mention_html()}! Введите имя пользователя GitHub, чтобы увидеть его активность.",
        parse_mode='HTML',
    )

# Команда /activity
async def activity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        username = context.args[0]
        activity_data = get_github_activity(username)
        if activity_data:
            # Генерируем уникальный ключ
            activity_key = str(uuid.uuid4())
            # Сохраняем данные в локальное хранилище
            activity_storage.save(activity_key, activity_data)
            # Передаем только ключ через URL
            web_app_url = f"{WEB_APP_URL}?key={activity_key}"
            keyboard = [[InlineKeyboardButton("Открыть активность", web_app={"url": web_app_url})]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text("Нажмите кнопку, чтобы открыть активность:", reply_markup=reply_markup)
        else:
            await update.message.reply_text("Не удалось получить данные о пользователе.")
    else:
        await update.message.reply_text("Пожалуйста, укажите имя пользователя GitHub.")

# Запуск бота
if __name__ == "__main__":
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("activity", activity))
    application.run_polling()

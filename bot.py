import os
import asyncio
import threading
import logging
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Setup Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

# Telegram Bot function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm alive 🚀")

async def telegram_bot():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    logging.info("Starting bot with token...")
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    await application.initialize()
    await application.start()
    logging.info("Bot started polling...")
    await application.updater.start_polling()
    await application.updater.idle()

def run_telegram_bot():
    asyncio.run(telegram_bot())

if __name__ == "__main__":
    # Start Telegram bot in background thread
    threading.Thread(target=run_telegram_bot, daemon=True).start()

    # Start Flask app
    app.run(host="0.0.0.0", port=8080)


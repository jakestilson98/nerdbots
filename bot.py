# STEP 1: Import Telegram libraries
from telegram.ext import Updater

# STEP 2: Read your Telegram key from file
telegram_key = open('TELEGRAM_KEY.txt').read().strip()

# STEP 3: Start the bot
updater = Updater(token=telegram_key)
updater.start_polling()

# STEP 4: Confirm it's running
print("BOT STATUS: Online! Message your bot to test.")

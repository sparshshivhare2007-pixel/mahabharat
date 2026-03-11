from telegram import Update
from telegram.ext import ContextTypes

async def shop(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
🛒 shop

1. गदा
2. धनुष
3. कवच
"""

    await update.message.reply_text(text)

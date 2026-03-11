from telegram import Update
from telegram.ext import ContextTypes

async def exile_event(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
🌲 वनवास

पांडवों को 13 वर्ष का वनवास मिला

उन्होंने शक्ति और ज्ञान प्राप्त किया
"""

    await update.message.reply_text(text)

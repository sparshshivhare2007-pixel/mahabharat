from telegram import Update
from telegram.ext import ContextTypes

async def shankhnaad(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
📯 शंखनाद

युद्ध प्रारम्भ
"""

    await update.message.reply_text(text)

from telegram import Update
from telegram.ext import ContextTypes

async def gita_jayanti(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
📜 गीता जयंती

भगवद गीता का ज्ञान

"कर्मण्येवाधिकारस्ते"

+150 धर्म
"""

    await update.message.reply_text(text)

from telegram import Update
from telegram.ext import ContextTypes

async def duel(update:Update,context:ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
"""⚔ द्वंद्व युद्ध

यह फीचर जल्द आएगा
"""
)

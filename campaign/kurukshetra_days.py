from telegram import Update
from telegram.ext import ContextTypes

async def war_days(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
⚔ कुरुक्षेत्र युद्ध

18 दिनों तक युद्ध चला

भीष्म
द्रोण
कर्ण

सब युद्ध में गिरे
"""

    await update.message.reply_text(text)

from telegram import Update
from telegram.ext import ContextTypes

async def temple(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
🛕 मंदिर

तुमने श्रीकृष्ण के दर्शन किए

+10 धर्म
"""

    await update.message.reply_text(text)

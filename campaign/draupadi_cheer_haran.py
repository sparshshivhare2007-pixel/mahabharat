from telegram import Update
from telegram.ext import ContextTypes

async def draupadi_event(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
⚠ सभा का अपमान

दुर्योधन और दुःशासन ने
द्रौपदी का अपमान किया

द्रौपदी ने पुकारा

"हे कृष्ण मेरी रक्षा करो"

🕉 श्रीकृष्ण ने उसकी लाज बचाई
"""
    await update.message.reply_text(text)

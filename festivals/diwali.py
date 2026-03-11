from telegram import Update
from telegram.ext import ContextTypes

async def diwali(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
🪔 दिवाली

प्रकाश का पर्व

+300 सुवर्ण
"""

    await update.message.reply_text(text)

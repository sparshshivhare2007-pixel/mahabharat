from telegram import Update
from telegram.ext import ContextTypes

async def janmashtami(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
🕉 जन्माष्टमी

आज श्रीकृष्ण का जन्मदिन है

+200 धर्म
+200 सुवर्ण
"""

    await update.message.reply_text(text)

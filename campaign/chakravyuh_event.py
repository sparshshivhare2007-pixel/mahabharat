from telegram import Update
from telegram.ext import ContextTypes

async def chakravyuh(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
⚔ चक्रव्यूह

कौरवों ने चक्रव्यूह रचना बनाई

अभिमन्यु इसमें प्रवेश करता है
"""

    await update.message.reply_text(text)

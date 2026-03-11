from telegram import Update
from telegram.ext import ContextTypes

async def abhimanyu_fall(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
💔 अभिमन्यु

अभिमन्यु वीरता से लड़ा

परंतु कौरवों ने मिलकर
उसे मार दिया

यह युद्ध का सबसे दुखद क्षण था
"""

    await update.message.reply_text(text)

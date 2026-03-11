from telegram import Update
from telegram.ext import ContextTypes

async def war_announce(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
📯 शंखनाद

कुरुक्षेत्र का युद्ध आरम्भ होने वाला है

पांडव और कौरव आमने सामने हैं

तैयार हो जाओ
"""
    await update.message.reply_text(text)

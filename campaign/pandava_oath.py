from telegram import Update
from telegram.ext import ContextTypes

async def pandava_oath(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
⚔ प्रतिज्ञा

भीम ने प्रतिज्ञा ली

दुःशासन का अंत होगा
और दुर्योधन का वध होगा

धर्म की रक्षा होगी
"""

    await update.message.reply_text(text)

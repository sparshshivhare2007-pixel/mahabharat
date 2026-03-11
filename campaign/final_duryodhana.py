from telegram import Update
from telegram.ext import ContextTypes

async def final_duryodhana(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
🏆 अंतिम युद्ध

भीम और दुर्योधन का गदा युद्ध

भीम ने दुर्योधन को पराजित किया

धर्म की विजय हुई
"""

    await update.message.reply_text(text)

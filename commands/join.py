from telegram import Update
from telegram.ext import ContextTypes

from database.mongo import battle_stats

async def join(update:Update,context:ContextTypes.DEFAULT_TYPE):

    chat = update.effective_chat.id

    await battle_stats.update_one(
        {"chat":chat},
        {"$set":{
            "boss":"दुर्योधन",
            "hp":5000,
            "active":True
        }},
        upsert=True
    )

    await update.message.reply_text(
"""📯 शंखनाद हुआ

दुर्योधन रणभूमि में उतर चुका है

/attack
/special
"""
)

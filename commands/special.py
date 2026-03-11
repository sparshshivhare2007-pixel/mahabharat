from telegram import Update
from telegram.ext import ContextTypes

from database.mongo import battle_stats
from game.battle_engine import special_attack

async def special(update:Update,context:ContextTypes.DEFAULT_TYPE):

    chat = update.effective_chat.id

    battle = await battle_stats.find_one({"chat":chat})

    if not battle:
        await update.message.reply_text("कोई युद्ध नहीं चल रहा")
        return

    damage = special_attack(1)

    hp = battle["hp"] - damage

    if hp <= 0:

        await battle_stats.delete_one({"chat":chat})

        await update.message.reply_text(
"""⚡ दिव्य प्रहार

दुर्योधन गिर चुका है
"""
)

        return

    await battle_stats.update_one(
        {"chat":chat},
        {"$set":{"hp":hp}}
    )

    await update.message.reply_text(
f"⚡ special attack\n\nक्षति {damage}\nHP {hp}"
)

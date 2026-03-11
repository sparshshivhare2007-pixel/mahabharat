from telegram import Update
from telegram.ext import ContextTypes

from database.mongo import battle_stats
from game.battle_engine import normal_attack

async def attack(update:Update,context:ContextTypes.DEFAULT_TYPE):

    chat = update.effective_chat.id

    battle = await battle_stats.find_one({"chat":chat})

    if not battle:
        await update.message.reply_text("कोई युद्ध नहीं चल रहा")
        return

    damage = normal_attack(1)

    hp = battle["hp"] - damage

    if hp <= 0:

        await battle_stats.delete_one({"chat":chat})

        await update.message.reply_text(
"""🏆 दुर्योधन पराजित

धर्म की विजय हुई
"""
)

        return

    await battle_stats.update_one(
        {"chat":chat},
        {"$set":{"hp":hp}}
    )

    await update.message.reply_text(
f"⚔ हमला\n\nक्षति {damage}\nबॉस HP {hp}"
)

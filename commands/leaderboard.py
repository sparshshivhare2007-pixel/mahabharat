from telegram import Update
from telegram.ext import ContextTypes

from database.mongo import users

async def leaderboard(update:Update,context:ContextTypes.DEFAULT_TYPE):

    top = users.find().sort("level",-1).limit(10)

    text = "🏆 leaderboard\n\n"

    i = 1

    async for user in top:

        text += f"{i}. {user['name']} - lvl {user['level']}\n"
        i += 1

    await update.message.reply_text(text)

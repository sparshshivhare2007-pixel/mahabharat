from telegram import Update
from telegram.ext import ContextTypes

async def help_cmd(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
📜 ᴄᴏᴍᴍᴀɴᴅs

/start
/profile
/balance
/daily
"""

    await update.message.reply_text(text)

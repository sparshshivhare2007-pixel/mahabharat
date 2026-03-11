from telegram import Update
from telegram.ext import ContextTypes

async def ramayan_teaser(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = """
📜 नई कथा

महाभारत समाप्त

अब आने वाली है

रामायण
"""

    await update.message.reply_text(text)

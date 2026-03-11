from telegram.ext import ApplicationBuilder, CommandHandler

from config import BOT_TOKEN

from commands.start import start
from commands.help import help_cmd
from commands.profile import profile
from commands.balance import balance
from commands.daily import daily

def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("profile", profile))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("daily", daily))

    print("ᴍᴀʜᴀʙʜᴀʀᴀᴛ ʙᴏᴛ ɪs ʀᴜɴɴɪɴɢ")

    app.run_polling()

if __name__ == "__main__":
    main()

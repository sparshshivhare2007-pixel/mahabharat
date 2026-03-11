from database.mongo import users

async def broadcast(bot,text):

    async for user in users.find():

        try:
            await bot.send_message(user["user_id"],text)
        except:
            pass

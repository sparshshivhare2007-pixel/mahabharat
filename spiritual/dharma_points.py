from database.mongo import users

async def add_dharma(user_id, points):

    await users.update_one(
        {"user_id": user_id},
        {"$inc": {"dharma": points}}
    )

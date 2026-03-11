from database.mongo import users

async def add_money(user_id, amount):

    await users.update_one(
        {"user_id": user_id},
        {"$inc": {"balance": amount}}
    )


async def remove_money(user_id, amount):

    await users.update_one(
        {"user_id": user_id},
        {"$inc": {"balance": -amount}}
    )

from database.mongo import users

async def get_user(user_id):
    return await users.find_one({"user_id": user_id})


async def create_user(user):

    data = {
        "user_id": user.id,
        "name": user.full_name,
        "balance": 100,
        "level": 1,
        "xp": 0,
        "dharma": 10,
        "wins": 0,
        "losses": 0
    }

    await users.insert_one(data)

    return data

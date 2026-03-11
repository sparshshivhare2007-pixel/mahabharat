from database.mongo import battle_stats

async def get_stats(user_id):
    return await battle_stats.find_one({"user_id": user_id})


async def create_stats(user_id):

    data = {
        "user_id": user_id,
        "wins": 0,
        "losses": 0
    }

    await battle_stats.insert_one(data)

from database.mongo import dharma

async def get_dharma(user_id):
    return await dharma.find_one({"user_id": user_id})


async def create_dharma(user_id):

    data = {
        "user_id": user_id,
        "points": 10
    }

    await dharma.insert_one(data)

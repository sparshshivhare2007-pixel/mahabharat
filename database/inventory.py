from database.mongo import inventory

async def get_inventory(user_id):
    return await inventory.find_one({"user_id": user_id})


async def create_inventory(user_id):

    data = {
        "user_id": user_id,
        "items": []
    }

    await inventory.insert_one(data)

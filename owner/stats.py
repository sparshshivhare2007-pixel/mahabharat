from database.mongo import users

async def total_users():

    return await users.count_documents({})

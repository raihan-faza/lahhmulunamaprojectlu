from pypika.terms import JSON

from models.users import User


async def create_account(username: str, password: str) -> dict:
    try:
        await User.create(username=username, password=password)
    except:
        return {"message": "failed to create user"}
    return {"message": "user created succesfully"}


async def delete_account(account_id: int) -> dict:
    # authorize here
    try:
        await User.filter(id=account_id).delete()
    except:
        return {"message": "failed to delete user"}
    return {"message": "user deleted succesfully"}


async def update_account(account_id: int, username: str, password: str):
    # authorize here
    try:
        user = await User.filter(id=account_id)
    except:
        return {"message": "failed to update user"}
    return {"message": "user updated succesfully"}


async def get_account(account_id: int):
    try:
        user = await User.get_or_none(id=account_id)
    except:
        return {"message": "user not found"}
    return {"user": user}

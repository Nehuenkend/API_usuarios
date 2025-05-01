from pydantic import BaseModel
from bson import Optional


def user_schema(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
    }


def users_schema(users) -> list:
    return [user_schema(user) for user in users]


class User(BaseModel):  # modelo de usuario
    id: int
    name: str
    surname: str
    age: int


class UserDB(BaseModel):  # modelo de usuario
    id: Optional[str] = None  # MongoDB crea el id por defecto
    username: str
    email: str

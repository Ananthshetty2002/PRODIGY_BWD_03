# app/services/auth_service.py

from app.models.user import fake_users_db
from app.utils.security import hash_password, verify_password, create_access_token

class AuthService:

    @staticmethod
    def register(username: str, password: str):
        if username in fake_users_db:
            return None
        hashed = hash_password(password)
        fake_users_db[username] = {"username": username, "password": hashed}
        return {"username": username}

    @staticmethod
    def login(username: str, password: str):
        user = fake_users_db.get(username)
        if not user or not verify_password(password, user["password"]):
            return None
        return create_access_token({"sub": username})

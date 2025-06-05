# app/routes/auth.py

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.schemas.user import UserRegister, UserLogin, Token
from app.services.auth_service import AuthService
from app.utils.security import decode_token

router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.post("/register")
def register(data: UserRegister):
    user = AuthService.register(data.username, data.password)
    if not user:
        raise HTTPException(status_code=400, detail="User already exists")
    return {"message": "User created", "user": user}

@router.post("/login", response_model=Token)
def login(data: UserLogin):
    token = AuthService.login(data.username, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token}

@router.get("/protected")
def protected(token: str = Depends(oauth2_scheme)):
    user = decode_token(token)
    if not user or not user.username:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return {"message": f"Hello {user.username}, you're authenticated!"}

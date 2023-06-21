from dataclasses import dataclass
from firebase_admin import auth
from fastapi import HTTPException

@dataclass
class User:
    id: str
    email: str
    name: str

def create_user(user_data):
    try:
        user = auth.create_user(
            email=user_data.email,
            password=user_data.password,
            display_name=user_data.name,
        )
        return User(id=user.uid, email=user.email, name=user.display_name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_user(email):
    try:
        user = auth.get_user_by_email(email)
        return User(id=user.uid, email=user.email, name=user.display_name)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

def authenticate_user(user_data):
    try:
        user = auth.get_user_by_email(user_data.email)
        if user and user.password == user_data.password:
            return User(id=user.uid, email=user.email, name=user.display_name)
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

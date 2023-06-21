from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from firebase_admin import credentials, auth, initialize_app
import openai

from user import User, create_user, get_user, authenticate_user
from openai_request import request_openai

app = FastAPI()

cred = credentials.Certificate("path/to/firebase/credentials.json")
initialize_app(cred)

openai.api_key = "your_openai_api_key"

class UserCreate(BaseModel):
    email: str
    password: str
    name: str

class UserAuth(BaseModel):
    email: str
    password: str

class OpenAIRequest(BaseModel):
    text: str

@app.post("/users")
def create_user_endpoint(user: UserCreate):
    return create_user(user)

@app.get("/users/{email}")
def get_user_endpoint(email: str):
    return get_user(email)

@app.post("/auth")
def authenticate_user_endpoint(user: UserAuth):
    return authenticate_user(user)

@app.post("/openai")
def request_openai_endpoint(request: OpenAIRequest, user: User = Depends(authenticate_user)):
    authenticate_user(user)
    return request_openai(request.text)

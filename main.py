from fastapi import FastAPI, Request, Response, Depends, status, HTTPException
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
import jwt

app = FastAPI()

secret_key = 'Your secret key'
algorithm = 'HS256'

class User(BaseModel):
    email : str
    password : str

db = [
    {'email': 'test@test.com', 'password': '123', 
     'user_id': '6786xcvn', 'coins': 50},

    {'email': 'test123@test.com', 'password': '555', 
     'user_id': '63xzytbn', 'coins': 150},
]

def find_user_by_id(user_id):
    for user in db:
        if user['user_id'] == user_id:
            return user

def find_user(email, password):
    for user in db:
        if user['email'] == email and user['password'] == password:
            return user
        

def generate_token(user_id):
    return jwt.encode(
        payload = {
            'user_id': user_id,
            'exp': datetime.now(timezone.utc) + timedelta(days = 7)
        },
        key = secret_key,
        algorithm = algorithm
    )


def decode_token(token):
    try:
        return jwt.decode(
            token,
            key = secret_key,
            algorithms = algorithm
        )
    
    except:
        return False
    

def get_user(req : Request):
    token = req.cookies.get('token', None)
    if token:
        payload = decode_token(token = token)
        if payload:
            user = find_user_by_id(user_id = payload['user_id'])
            return user
        

@app.post('/login')
def login(user_data : User, res : Response):
    # check if user exsists
    user = find_user(user_data.email, user_data.password)
    if user:
        # create jwt token 
        token = generate_token(user_id = user['user_id'])
        res.set_cookie(
            key = 'token',
            value = token,
            expires = datetime.now(timezone.utc) + timedelta(days = 7),
            httponly = True
        )

        return {'msg': 'You are logedin'}
    
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = 'Incorrect email or password'
    )


@app.get('/dashboard')
def dashboard(req : Request, user = Depends(get_user)):
    if user:
        return {'email': user['email'], 'coins': user['coins']}
    
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = 'You are not authorized to view this page'
    )

from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
import uvicorn
import os 
from src.summarizer import build_agent
from pymongo import MongoClient
from bson import ObjectId
import datetime
import json 

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

agent = build_agent()


# Personal
# MONGO_URI = "mongodb+srv://92vasim:gRfZDke1SRvtOWVE@tutorials.sb6u7w5.mongodb.net" 

# Project chatgpt warriors
# MONGO_URI = "mongodb+srv://92khatir:5KMck0oYUw6pi5eP@cluster0.he9jkpa.mongodb.net/"

# client = MongoClient(MONGO_URI)

# db = client["exploresheet-users"]

# user_db = db.users

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/", response_class=HTMLResponse)
# async def login(request: Request):

#     data_folder = "data"
#     delete_files_in_folder(data_folder)

#     return templates.TemplateResponse("signin.html", {"request": request})


# @app.post("/home", response_class=HTMLResponse)
# async def login(
#     request: Request, 
#     email: Annotated[str, Form()]
# ):

#     data_folder = "data"
#     delete_files_in_folder(data_folder)

#     user = user_db.find_one({"email": email})
#     print(user)

#     try:

#     # Check if the email exists in the db
#         if email != user['email']:
#             return templates.TemplateResponse("signin.html", {"request": request, "message":"Sorry! User is not found. Please sign up yourself."})
#         else:
#             return templates.TemplateResponse("index.html", {"request": request})
    
#     except Exception as e:
#             print(e)
#             return templates.TemplateResponse("signin.html", {"request": request, "message":"Sorry! User is not found. Please sign up yourself."})


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/chat", response_class=HTMLResponse)
async def chat(
    request: Request
    ):

    return templates.TemplateResponse("chat.html", {"request": request})
    

@app.get("/response")
async def response(
        chat: str 
        ):
    # print(type(chat))
    if agent is None:
        return {"message": "Sorry for inconvenience"}
    else:
        try:
            res = agent.run(chat)
            print(res)
            return {"res": res}
        except Exception as e:
            res = "Sorry! System is not available to response. Please try again later."
            print(e)
            return {"res": res}




# @app.get("/signup", response_class=HTMLResponse)
# async def signup(request: Request):
    
#     return templates.TemplateResponse("signup.html", {"request": request})

# @app.post("/signup", response_class=HTMLResponse)
# async def home(
#     request: Request,
#     name: Annotated[str, Form()], 
#     email: Annotated[str, Form()],
#     phone: Annotated[str, Form()]
# ):
#     user = {
#         "name": name,
#         "email": email,
#         "phone": phone,
#         "date": datetime.datetime.today()
#     }

#     print(user)

#     user_db.insert_one(user)

#     data_folder = "data"
#     delete_files_in_folder(data_folder)
    
#     return templates.TemplateResponse("signin.html", {"request": request, "name": name})


if __name__ == "__main__":
    # Production
    # uvicorn.run("app:app", port=6654, host="0.0.0.0")

    # Local
    uvicorn.run("app:app", port=8823, reload=True)


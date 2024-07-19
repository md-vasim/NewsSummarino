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
import gradio as gr 

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

templates = Jinja2Templates(directory="templates")

agent = build_agent()

# helper functions
def answer_query(message, history):
    message = agent.run(message)
    return message

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})


# chat ui
newsbot = gr.Chatbot(label="News Summarino", show_copy_button=True)
textbox = gr.Textbox(scale=9)
examples = ["Latest AI news", "AI in Hyderabad since the last year"]
with gr.Blocks(
    title="News Summarino Chat",
    css="footer {visibility: hidden}"
) as chatui:
    gr.Markdown("# <center> Welcome to News Summarino </center>")
    # gr.Examples(examples=examples, inputs=[textbox])
    gr.ChatInterface(fn=answer_query, chatbot=newsbot, textbox=textbox, theme="soft", submit_btn="Ask", undo_btn=None, retry_btn=None, clear_btn=None)
    print("Chat interface is cool.")
    gr.Markdown("<center> Developed by Mohammed Vasim | AI Engineer @ ChatGPT Warriors.  </center>")

# mounting at the path
app = gr.mount_gradio_app(app, chatui, path="/newssummarino")


if __name__ == "__main__":
    # Local
    uvicorn.run("app:app", port=8823, reload=True)


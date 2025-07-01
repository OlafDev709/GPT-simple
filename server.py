import os
import openai
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv() #load env vars from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
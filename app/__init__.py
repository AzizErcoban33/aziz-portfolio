import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    about_text = (
        "I am a Computer Science student at Trinity College Dublin, interested in "
        "backend development, systems, production engineering, and building useful "
        "software projects. I enjoy learning by creating real projects and improving "
        "them step by step."
    )

    return render_template(
        'index.html',
        title="Aziz Ercoban",
        url=os.getenv("URL"),
        about_text=about_text
    )

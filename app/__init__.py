import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    about_text = (
        "I am an Integrated Computer Science student at Trinity College Dublin with a strong "
        "interest in backend engineering, AI systems, production engineering, and data-driven "
        "applications. I enjoy building real projects with Python, Flask, Django, FastAPI, SQL, "
        "Docker, and search/retrieval systems, and I like improving my work step by step through "
        "practical engineering."
    )

    experiences = [
        {
            "role": "Backend & AI Engineer",
            "company": "Propylon – AI-Native Legislative Research Platform",
            "dates": "Dec 2025 - Mar 2026",
            "description": (
                "Worked on backend and AI features for a legislative research platform, including "
                "Congress.gov data ingestion, legal-text chunking, embedding generation, search "
                "indexing, semantic retrieval, reranking, caching, and citation validation."
            ),
        },
        {
            "role": "Backend Developer",
            "company": "Flight Data Analysis Project",
            "dates": "Oct 2025 - Dec 2025",
            "description": (
                "Developed backend workflows using SQL and pandas to store, process, and analyze "
                "flight data, making the analysis pipeline more reliable and reusable."
            ),
        },
    ]

    education_items = [
        {
            "school": "Trinity College Dublin",
            "degree": "Integrated Computer Science (B.A. (Mod.))",
            "dates": "Sept 2024 - May 2028",
            "description": (
                "Currently studying Computer Science with First Class Honours performance. "
                "Relevant areas include data structures and algorithms, systems programming, "
                "applied probability and statistics, databases, computer architecture, digital "
                "logic, and software engineering."
            ),
        },
    ]

    hobbies = [
        {
            "name": "Gym and Fitness",
            "description": "I enjoy training consistently and improving my strength, discipline, and health.",
        },
        {
            "name": "Travel",
            "description": "I like exploring new places, cultures, and cities whenever I get the chance.",
        },
        {
            "name": "Building Projects",
            "description": "I enjoy turning ideas into real software projects and learning by doing.",
        },
    ]

    return render_template(
        'index.html',
        title="Aziz Ercoban",
        url=os.getenv("URL"),
        about_text=about_text,
        experiences=experiences,
        education_items=education_items,
        hobbies=hobbies,
    )
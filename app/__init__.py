import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


ABOUT_TEXT = (
    "I am an Integrated Computer Science student at Trinity College Dublin with a strong "
    "interest in backend engineering, AI systems, production engineering, and data-driven "
    "applications. I enjoy building real projects with Python, Flask, Django, FastAPI, SQL, "
    "Docker, and search/retrieval systems, and I like improving my work step by step through "
    "practical engineering."
)

EXPERIENCES = [
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

EDUCATION_ITEMS = [
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

HOBBIES = [
    {
        "name": "Traveling",
        "description": (
            "I enjoy visiting new places, experiencing different cultures, and learning "
            "from the cities and countries I travel to."
        ),
        "image": "travel.jpeg",
    },
    {
        "name": "Building Projects",
        "description": (
            "I like turning ideas into real software projects and improving them step by step "
            "while learning new technologies."
        ),
        "image": "project.jpeg",
    },
    {
        "name": "Animals",
        "description": (
            "I enjoy spending time around animals and I like how they bring calmness, energy, "
            "and personality into everyday life."
        ),
        "image": "animal.jpeg",
    },
]

PLACES_VISITED = [
    {
        "name": "Dublin, Ireland",
        "description": "Where I study at Trinity College Dublin.",
        "latitude": 53.3498,
        "longitude": -6.2603,
    },
    {
        "name": "Nicosia, Cyprus",
        "description": "A place connected to my home and personal background.",
        "latitude": 35.1856,
        "longitude": 33.3823,
    },
    {
        "name": "Kyrenia, Cyprus",
        "description": "One of the beautiful coastal places I enjoy in Cyprus.",
        "latitude": 35.3403,
        "longitude": 33.3192,
    },
    {
        "name": "Berlin, Germany",
        "description": "One of the places I have visited in Germany.",
        "latitude": 52.5200,
        "longitude": 13.4050,
    },
    {
        "name": "Athens, Greece",
        "description": "One of the places I have visited in Greece.",
        "latitude": 37.9838,
        "longitude": 23.7275,
    },
]

NAV_LINKS = [
    {
        "name": "Home",
        "endpoint": "index",
    },
    {
        "name": "Hobbies",
        "endpoint": "hobbies_page",
    },
]


@app.context_processor
def inject_nav_links():
    return {
        "nav_links": NAV_LINKS
    }


@app.route('/')
def index():
    return render_template(
        'index.html',
        title="Aziz Ercoban",
        url=os.getenv("URL"),
        about_text=ABOUT_TEXT,
        experiences=EXPERIENCES,
        education_items=EDUCATION_ITEMS,
        hobbies=HOBBIES,
        places_visited=PLACES_VISITED,
    )


@app.route('/hobbies')
def hobbies_page():
    return render_template(
        'hobbies.html',
        title="Hobbies | Aziz Ercoban",
        url=os.getenv("URL"),
        hobbies=HOBBIES,
    )
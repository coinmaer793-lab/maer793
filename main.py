from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


# Главная страница
@app.get("/", response_class=HTMLResponse)
def home():
    html_file = Path("templates/index.html")
    return html_file.read_text(encoding="utf-8")


# Страницы тренировок
@app.get("/training-numbers", response_class=HTMLResponse)
def training_numbers():
    html_file = Path("templates/training-numbers.html")
    return html_file.read_text(encoding="utf-8")


@app.get("/training-spets", response_class=HTMLResponse)
def training_spets():
    html_file = Path("templates/training-spets.html")
    return html_file.read_text(encoding="utf-8")


@app.get("/training-memory", response_class=HTMLResponse)
def training_memory():
    html_file = Path("templates/training-memory.html")
    return html_file.read_text(encoding="utf-8")


@app.get("/training-speed", response_class=HTMLResponse)
def training_speed():
    html_file = Path("templates/training-speed.html")
    return html_file.read_text(encoding="utf-8")


@app.get("/training-story", response_class=HTMLResponse)
def training_story():
    html_file = Path("templates/training-story.html")
    return html_file.read_text(encoding="utf-8")


@app.get("/health")
def health_check():
    return {"status": "ok"}

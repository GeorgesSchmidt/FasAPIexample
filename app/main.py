from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from .models import Note

# Crée la base de données si elle n'existe pas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Notes Web App")
templates = Jinja2Templates(directory="app/templates")


# Dépendance pour obtenir une session SQLAlchemy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Page d'accueil affichant toutes les notes
@app.get("/", response_class=HTMLResponse)
def read_notes(request: Request, db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    return templates.TemplateResponse("index.html", {"request": request, "notes": notes})


# Route pour ajouter une note via le formulaire HTML
@app.post("/add_note")
def add_note(title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    note = Note(title=title, content=content)
    db.add(note)
    db.commit()
    return {"message": "Note added!"}

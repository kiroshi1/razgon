from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(title=settings.PROJECT_NAME)


@app.get("/hello")
def hello_world(db: Annotated[Session, Depends(get_db)]):
    return {"message": f"Hello from {settings.PROJECT_NAME}!"}
    return {"message": f"Hello from {settings.PROJECT_NAME}!"}

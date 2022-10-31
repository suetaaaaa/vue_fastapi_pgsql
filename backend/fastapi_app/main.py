from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()




@app.get('/li')
def get_li(db: Session = Depends(get_db)):
	all_li = crud.get_all_li(db)

	return all_li
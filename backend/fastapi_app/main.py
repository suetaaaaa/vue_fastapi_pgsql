from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from . import crud, models
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
	'http://127.0.0.1:5174',
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=['*'],
	allow_headers=['*'],
)

# Dependency
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()



@app.get('/li')
async def get_li(db: Session = Depends(get_db)):
	all_li = await crud.get_all_li(db)

	return all_li
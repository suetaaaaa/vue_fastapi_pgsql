from sqlalchemy.orm import Session

from . import models



async def get_all_li(db: Session):
	
	return db.query(models.Li).all()

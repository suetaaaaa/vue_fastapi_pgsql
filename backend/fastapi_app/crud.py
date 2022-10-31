from sqlalchemy.orm import Session

from . import models



def get_all_li(db: Session):
	
	return db.query(models.Li).all()

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from .database import Base

import uuid



class Li(Base):
	__tablename__ = 'li'

	id = Column(Integer, index=True)
	ord = Column(Integer, index=True)
	name = Column(String, index=True)
	code = Column(String, index=True)
	kis_nt_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid1, index=True)
	act = Column(Boolean, index=True)
	dt = Column(DateTime(timezone=False), server_default=func.current_time(), index=True)

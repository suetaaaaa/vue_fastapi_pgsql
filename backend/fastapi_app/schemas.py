from pydantic import BaseModel
from typing import Optional, Union

from datetime import datetime, time
from uuid import UUID



class LiBase(BaseModel):
	id: int
	ord: int
	name: str 
	code: str 
	act: bool
	dt: datetime



class Li(LiBase):
	kis_nt_id: Union[int, str, UUID]

	class Config:
		orm_mode = True

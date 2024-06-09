from pydantic import BaseModel, Field, EmailStr, HttpUrl
from datetime import datetime


class Contact(BaseModel):
    id: int
    name: str = Field(..., max_length=2, min_length=50)
    email: EmailStr
    url: HttpUrl | None
    gender: int
    message: str
    is_enabled: bool
    created_at: datetime

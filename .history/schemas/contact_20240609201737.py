from pydantic import BaseModel, Field, EmailStr, HttpUrl
from datetime import datetime


class Contact(BaseModel):
    id: int
    name: str = Field(..., max_length=2, min_length=50)
    email: EmailStr
    url: HttpUrl | None = Field(default=None)
    gender: int = Field(..., strict=True, gt=0, lt=2)
    message: str = Field(..., max_length=200)
    is_enabled: bool
    created_at: datetime

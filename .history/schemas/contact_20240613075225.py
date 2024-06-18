from pydantic import BaseModel, Field, EmailStr, HttpUrl
from datetime import datetime


class ContactBase(BaseModel):

    name: str = Field(..., max_length=50, min_length=2)
    email: EmailStr
    url: HttpUrl | None = Field(default=None)
    gender: int = Field(..., strict=True, ge=0, le=2)
    message: str = Field(..., max_length=200)
    is_enabled: bool = Field(default=False)

    class Config:
        orm_mode = True

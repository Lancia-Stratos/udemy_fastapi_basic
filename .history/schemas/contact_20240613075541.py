from pydantic import BaseModel, Field, EmailStr, HttpUrl
from datetime import datetime


class ContactList(BaseModel):
    id: int
    name: str = Field(..., max_length=50, min_length=2)
    created_at: datetime

    class Config:
        from_attribute = True


class ContactBase(BaseModel):

    name: str = Field(..., max_length=50, min_length=2)
    email: EmailStr
    url: HttpUrl | None = Field(default=None)
    gender: int = Field(..., strict=True, ge=0, le=2)
    message: str = Field(..., max_length=200)
    is_enabled: bool = Field(default=False)

    class Config:
        from_attribute = True


class ContactDetail(ContactBase):
    id: int
    created_at: datetime

    class Config:
        from_attribute = True


class ContactCreate(ContactBase):
    pass
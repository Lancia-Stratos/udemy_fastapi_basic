from pydantic import BaseModel, Field


class Contact(BaseModel):
    name: str
    email: str
    phone: str
    message: str

from pydantic import BaseModel, Field
from datetime import datetime


class Contact(BaseModel):
    name: str
    email: str
    phone: str
    message: str

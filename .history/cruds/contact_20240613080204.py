from sqlalchemy.ext.asyncio import AsyncSession

from models.contact import Contact
from schemas.contact import ContactCreate


async def create_contact(db: AsyncSession, contact_create: ContactCreate):
    contact = Contact(**contact_create.dict())
    db.add(contact)
    await db.commit()
    return contact

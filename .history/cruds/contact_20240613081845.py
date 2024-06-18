from sqlalchemy.ext.asyncio import AsyncSession

import schemas.contact as contact_schema
import models.contact as contact_model


async def create_contact(db: AsyncSession, contact: contact_schema.ContactCreate)->contact_model.Contact:

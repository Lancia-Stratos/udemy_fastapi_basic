from sqlalchemy.ext.asyncio import AsyncSession

import schemas.contact as contact_schema
import models.contact as contact_schema


async def create_contact(db: AsyncSession, contact: ):
   
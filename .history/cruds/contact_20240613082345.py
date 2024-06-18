from sqlalchemy.ext.asyncio import AsyncSession

import schemas.contact as contact_schema
import models.contact as contact_model


async def create_contact(
    db: AsyncSession, contact: contact_schema.ContactCreate
) -> contact_model.Contact:
    """
    DBに保存
    引数:
        db: DBセッション
        contact: 作成するコンタクトのデータ
    戻り値:
        作成されたORMモデル
    """

    contact.model_dump()

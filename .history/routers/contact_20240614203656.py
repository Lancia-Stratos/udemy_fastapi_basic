from multiprocessing import dummy
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import schemas.contact as contact_schema
import cruds.contact as contact_crud
from database import get_db

router = APIRouter()


@router.get("/contacts", response_model=list[contact_schema.ContactList])  # 一覧表示
async def get_contact_all():
    dummy_date = datetime.now()
    return [
        contact_schema.ContactList(
            id=1,
            name="山田",
            email="test@test.com",
            phone="090-1234-5678",
            url="https://test.com",
            gender=1,
            message="テスト",
            created_at=dummy_date,
            is_enabled=False,
        )
    ]


@router.post("/contacts", response_model=contact_schema.ContactCreate)  # 保存
async def create_contact(
    body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)
):
    return await contact_crud.create_contact(db, body)


@router.get("/contacts/{id}", response_model=contact_schema.ContactDetail)  # 詳細表示
async def get_contact(id: int, db: AsyncSession = Depends(get_db)):
    return await contact_crud.get_contact_by_id(db, id)


@router.put("/contacts/{id}", response_model=contact_schema.ContactCreate)  # 更新
async def update_contact(id: int, body: contact_schema.ContactCreate):
    return contact_schema.Contact(**body.model_dump())


@router.delete("/contacts/{id}", response_model=None)  # 削除
async def delete_contact(id: int):
    return


def get_message():
    message = "Hello World"
    print(f"get_messageが実行された: {message}")
    return message


@router.get("/depends")

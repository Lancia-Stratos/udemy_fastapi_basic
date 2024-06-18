from multiprocessing import dummy
from fastapi import APIRouter, Depends
from datetime import datetime
import schemas.contact as contact_schema

router = APIRouter()


@router.get("/contacts", response_model=list[contact_schema.Contact])  # 一覧表示
async def get_contact_all():
    dummy_date = datetime.now()
    return [
        contact_schema.Contact(
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


@router.post("/contacts", response_model=contact_schema.Contact)  # 保存
async def create_contact(body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())


@router.get("/contacts/{id}", response_model=contact_schema.Contact)  # 詳細表示
async def get_contact(id: int):
    return contact_schema.Contact(id)


@router.put("/contacts/{id}", response_model=contact_schema.Contact)  # 更新
async def update_contact(id: int, body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())


@router.delete("/contacts/{id}", response_model=contact_schema.Contact)  # 削除
async def delete_contact(id: int):
    return

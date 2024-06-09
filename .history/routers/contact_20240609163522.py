from multiprocessing import dummy
from fastapi import APIRouter
from datetime import datetime
import schemas.contact as contact_schema

router = APIRouter()


@router.get("/contacts", response_model=list[contact_schema.Contact])  # 一覧表示
async def get_contact_all():
    dummy_date = datetime.now()


@router.post("/contacts")  # 保存
async def create_contact():
    pass


@router.get("/contacts/{id}")  # 詳細表示
async def get_contact():
    pass


@router.put("/contacts/{id}")  # 更新
async def update_contact():
    pass


@router.delete("/contacts/{id}")  # 削除
async def delete_contact():
    pass

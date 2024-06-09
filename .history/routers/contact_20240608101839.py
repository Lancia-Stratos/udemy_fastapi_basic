from fastapi import APIRouter

router = APIRouter()


@router.get("/contacts")  # 一覧表示
async def get_contact_all():
    pass


@router.post("/contacts")  # 保存
async def create_contact():
    pass

@router.get("/contacts/{is}") # 詳細表示
async def get_contact():

@router.put("/contacts{id}") #更新
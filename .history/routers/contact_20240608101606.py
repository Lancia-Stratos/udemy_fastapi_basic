from fastapi import APIRouter

router = APIRouter()


@router.get("/contacts")
async def get_contact_all():
    pass

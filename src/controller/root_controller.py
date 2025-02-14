from fastapi import APIRouter
from src.service import root_service
from src.model import root_model

router = APIRouter(prefix="/api", tags=["接口"])


@router.get("/list", summary="列表")
async def findAll():
    return root_service.findAll()


@router.get("/{id}")
async def findOne(id: int):
    return root_service.findOne(id)


@router.put("/{id}")
async def update(id: int, item: root_model.RootModel):
    return root_service.update(id, item)


@router.post("/add")
async def create(item: root_model.RootModel):
    return root_service.create(item)


@router.delete("/{id}")
async def delete(id: int):
    return root_service.delete(id)

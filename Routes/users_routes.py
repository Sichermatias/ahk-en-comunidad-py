from fastapi import APIRouter, status, Request
from services.users_service import UsersService

_service = UsersService()

router = APIRouter()

@router.get("")
async def listar_usuarios():
    return _service.listar_usuarios()

@router.post("", status_code=status.HTTP_201_CREATED)
async def crear_usuario(request: Request):
    data = await request.json()

    return _service.crear_usuario(data)

@router.get("/{id}")
def obtener_usuario(id):
    return _service.obtener_usuario(int(id))

@router.put("/{id}")
async def actualizar_usuario(id, request: Request):
    data = await request.json()

    return _service.actualizar_usuario(int(id), data)
    

@router.get("/{id}/gustos-musicales")
def listar_gustos(id):
    return _service.listar_gustos(int(id))

@router.post("/{id}/gustos-musicales")
async def agregar_gustos(id, request: Request):
    data = await request.json()

    return _service.agregar_gustos(int(id), data)
    

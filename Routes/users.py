from fastapi import APIRouter, HTTPException, status, Request
from Services.users_service import UsersService
from repository.users_repository import UsersRepository


_repo = UsersRepository()
_service = UsersService(_repo)

router = APIRouter()

@router.get("")
async def listar_usuarios():
    return _service.listar_usuarios()

@router.post("", status_code=status.HTTP_201_CREATED)
async def crear_usuario(request: Request):
    data = await request.json()

    payload = {
        "nombre": data.get("nombre", ""),
        "apellido": data.get("apellido", ""),
        "email": data.get("email", ""),
        "fecha_nacimiento": data.get("fecha_nacimiento", ""),
        "biografia": data.get("biografia", ""),
        "provincia": data.get("provincia", ""),
        "localidad": data.get("localidad", ""),
        "gustos_musicales": data.get("gustos_musicales", []) or []
    }
    try:
        usuario_creado = _service.crear_usuario(**payload)
        return usuario_creado.__dict__
        
    except ValueError as e:
        if str(e) == "email_duplicado":
            raise HTTPException(status_code = 409, detail = "El email ya existe")
        raise

@router.get("/{id}")
def obtener_usuario(id):
    usuario = _service.obtener_usuario(id)
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
    return usuario.__dict__

@router.put("/{id}")
async def actualizar_usuario(id, request: Request):
    data = await request.json()
    
    usuario_actualizado = _service.actualizar_usuario(
        id,
        nombre=data.get("nombre"),
        apellido=data.get("apellido"),
        email=data.get("email"),
        fecha_nacimiento=data.get("fecha_nacimiento"),
        biografia=data.get("biografia"),
        provincia=data.get("provincia"),
        localidad=data.get("localidad"),
        gustos_musicales=data.get("gustos_musicales")
    )
    
    if not usuario_actualizado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
    return usuario_actualizado.__dict__

@router.post("/{id}/gustos-musicales")
async def agregar_gustos(id, request: Request):
    data = await request.json()
    
    gustos = data.get("gustos", [])
    
    if not isinstance(gustos, list):
        gustos = [str(gustos)]
        
    usuario_con_gustos = _service.agregar_gustos(id, gustos)
    
    if not usuario_con_gustos:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
    return {"gustos_musicales": usuario_con_gustos.gustos_musicales}

@router.get("/{id}/gustos-musicales")
def listar_gustos(id):
    usuario = _service.obtener_usuario(id)
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
    return {"gustos_musicales": usuario.gustos_musicales}

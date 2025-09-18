from repositories.users_repository import UsersRepository
from entities.user import Usuario
from fastapi import HTTPException

_repo = UsersRepository()

class UsersService:

    def crear_usuario(self, data):

        # Verificar si el email ya existe
        email = data.get("email", "").lower()
        if self.existe_email(email):
            raise HTTPException(status_code=409, detail="El email ya existe")
    
        biografia = data.get("biografia").strip()
        if len(biografia) > 500:
            raise HTTPException(status_code=400, detail="La biografía no puede tener más de 500 caracteres")

        # Crear instancia de Usuario
        usuario = Usuario(
            id=_repo.next_id(),
            nombre=data.get("nombre", "").strip(),
            apellido=data.get("apellido", "").strip(),
            email=email,
            fecha_nacimiento=str(data.get("fecha_nacimiento", "")),
            biografia=biografia,
            provincia=data.get("provincia", "").strip(),
            localidad=data.get("localidad", "").strip(),
            gustos_musicales=data.get("gustos_musicales", []) or []
        )

        # Guardar en el repositorio
        usuario_guardado = _repo.guardar(usuario)

        return usuario_guardado
    

    def existe_email(self, email: str) -> bool:
        return _repo.obtener_por_email(email) is not None


    def listar_usuarios(self):
        return _repo.listar_usuarios()


    def obtener_usuario(self, id):
        usuario = _repo.obtener(id)
    
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
            
        return usuario


    def actualizar_usuario(self, id, data):

        usuario = self.obtener_usuario(id)

        biografia = data.get("biografia").strip()
        if len(biografia) > 500:
            raise HTTPException(status_code=400, detail="La biografía no puede tener más de 500 caracteres")
            
        usuario.biografia = biografia if biografia else usuario.biografia
        usuario.email = data.get("email").strip().lower() if data.get("email") else usuario.email
        usuario.fecha_nacimiento = data.get("fecha_nacimiento").strip() if data.get("fecha_nacimiento") else usuario.fecha_nacimiento
        usuario.provincia = data.get("provincia").strip() if data.get("provincia") else usuario.provincia
        usuario.localidad = data.get("localidad").strip() if data.get("localidad") else usuario.localidad
        usuario.gustos_musicales = data.get("gustos_musicales") if data.get("gustos_musicales") else usuario.gustos_musicales
        usuario.nombre = data.get("nombre").strip() if data.get("nombre") else usuario.nombre
        usuario.apellido = data.get("apellido").strip() if data.get("apellido") else usuario.apellido

        return _repo.actualizar(usuario)


    def agregar_gustos(self, id, data):
        usuario = self.obtener_usuario(id)

        gustos = data.get("gustos_musicales")
        gustos_normalizados = [str(gusto).strip().lower() for gusto in gustos]

        usuario.agregar_gustos(gustos_normalizados)
        
        return _repo.actualizar(usuario)


    def listar_gustos(self, id):
        usuario = self.obtener_usuario(id)
        
        return usuario.gustos_musicales
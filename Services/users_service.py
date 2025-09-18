from repositories.users_repository import UsersRepository
from entities.user import Usuario


class UsersService:
    def __init__(self, repo):
        self.repo = repo
    
    def email_existe(self, email: str) -> bool:
        """Verifica si un email ya existe en el sistema"""
        return self.repo.obtener_por_email(email) is not None

    def actualizar_usuario(self, id_, nombre=None, apellido=None, email=None, 
                          fecha_nacimiento=None, biografia=None, provincia=None, 
                          localidad=None, gustos_musicales=None):
        datos_actualizacion = {}
        
        if nombre is not None:
            datos_actualizacion['nombre'] = nombre.strip()
        if apellido is not None:
            datos_actualizacion['apellido'] = apellido.strip()
        if email is not None:
            datos_actualizacion['email'] = email.lower()
        if fecha_nacimiento is not None:
            datos_actualizacion['fecha_nacimiento'] = str(fecha_nacimiento)
        if biografia is not None:
            datos_actualizacion['biografia'] = biografia.strip()
        if provincia is not None:
            datos_actualizacion['provincia'] = provincia.strip()
        if localidad is not None:
            datos_actualizacion['localidad'] = localidad.strip()
        if gustos_musicales is not None:
            datos_actualizacion['gustos_musicales'] = list(dict.fromkeys([str(gusto).strip().lower() for gusto in gustos_musicales]))
        
        return self.repo.actualizar(id_, datos_actualizacion)

    def agregar_gustos(self, id_, gustos):
        gustos_norm = [str(gusto).strip().lower() for gusto in gustos]
        
        return self.repo.agregar_gustos(id_, gustos_norm)

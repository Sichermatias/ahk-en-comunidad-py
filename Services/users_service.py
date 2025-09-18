from repository.users_repository import UsersRepository, Usuario


class UsersService:
    def __init__(self, repo):
        self.repo = repo

    def listar_usuarios(self):
        return self.repo.listar_usuarios()

    def crear_usuario(self, *, nombre, apellido, email, fecha_nacimiento, biografia, provincia, localidad, gustos_musicales):
        if self.repo.obtener_por_email(email):
            raise ValueError("email_duplicado")
            
        usuario_creado = Usuario(
            id = self.repo.next_id(),
            nombre = nombre.strip(),
            apellido = apellido.strip(),
            email = email.lower(),
            fecha_nacimiento = str(fecha_nacimiento),
            biografia = biografia.strip(),
            provincia = provincia.strip(),
            localidad = localidad.strip(),
            gustos_musicales = list(dict.fromkeys([str(gusto).strip().lower() for gusto in gustos_musicales]))
        )
        
        return self.repo.crear(usuario_creado)

    def obtener_usuario(self, id_):
        return self.repo.obtener(id_)

    def actualizar_usuario(self, id_, **kwargs):
        return self.repo.actualizar(id_, **kwargs)

    def agregar_gustos(self, id_, gustos):
        gustos_norm = [str(gusto).strip().lower() for gusto in gustos]
        
        return self.repo.agregar_gustos(id_, gustos_norm)

from dataclasses import dataclass, field

@dataclass
class Usuario:
    id: int
    nombre: str
    apellido: str
    email: str
    fecha_nacimiento: str
    biografia: str
    provincia: str
    localidad: str
    gustos_musicales: list = field(default_factory=list)

class UsersRepository:
    def __init__(self):
        self._by_id = {}
        self._by_email = {}
        self._next_id = 1

    def next_id(self):
        current_id = self._next_id
        self._next_id += 1
        
        return current_id

    def listar_usuarios(self):
        return list(self._by_id.values())

    def crear(self, usuario):
        if usuario.email in self._by_email:
            raise ValueError("email_duplicado")
            
        self._by_id[usuario.id] = usuario
        self._by_email[usuario.email] = usuario.id
        
        return usuario

    def obtener(self, id_):
        return self._by_id.get(id_)

    def obtener_por_email(self, email):
        id_ = self._by_email.get(email)
        
        return self._by_id.get(id_) if id_ else None

    def actualizar(self, id_, datos_actualizacion):
        usuario = self._by_id.get(id_)
        
        if not usuario:
            return None
            
        for campo, valor in datos_actualizacion.items():
            if valor is not None and hasattr(usuario, campo):
                setattr(usuario, campo, valor)
                
        return usuario

    def agregar_gustos(self, id_, gustos):
        usuario = self._by_id.get(id_)
        
        if not usuario:
            return None
            
        existentes = set(usuario.gustos_musicales)
        
        for gusto in gustos:
            if gusto not in existentes:
                usuario.gustos_musicales.append(gusto)
                existentes.add(gusto)
                
        return usuario

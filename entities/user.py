from typing import List


class Usuario:
    def __init__(self, id: int, nombre: str, apellido: str, email: str, 
                 fecha_nacimiento: str, biografia: str, provincia: str, 
                 localidad: str, gustos_musicales: List[str] = None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.biografia = biografia
        self.provincia = provincia
        self.localidad = localidad
        self.gustos_musicales = gustos_musicales if gustos_musicales is not None else []
    
    def agregar_gusto_musical(self, gusto: str):
        """Agrega un gusto musical si no existe"""
        gusto_normalizado = str(gusto).strip().lower()
        if gusto_normalizado and gusto_normalizado not in self.gustos_musicales:
            self.gustos_musicales.append(gusto_normalizado)
    
    def eliminar_gusto_musical(self, gusto: str):
        """Elimina un gusto musical si existe"""
        gusto_normalizado = str(gusto).strip().lower()
        if gusto_normalizado in self.gustos_musicales:
            self.gustos_musicales.remove(gusto_normalizado)
    
    def __repr__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre}', email='{self.email}')"
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"

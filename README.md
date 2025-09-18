# EC - En Comunidad (FastAPI)

Una aplicación web simple para gestionar usuarios y sus gustos musicales, desarrollada con FastAPI siguiendo una arquitectura en capas.

## 🏗️ Arquitectura

El proyecto sigue una arquitectura en capas bien definida:

```
├── main.py                    # Punto de entrada de la aplicación
├── entities/
│   └── user.py               # Modelo de datos Usuario
├── repositories/
│   └── users_repository.py   # Capa de acceso a datos (almacenamiento en memoria)
├── services/
│   └── users_service.py      # Lógica
└── routes/
    └── users_routes.py       # Endpoints REST
```

## 🚀 Instalación y Ejecución

### Pasos para ejecutar

1. **Instalar dependencias:**
```bash
py -m pip install -r requirements.txt
```

2. **Ejecutar la aplicación:**
```bash
py -m uvicorn main:app --reload
```

3. **Acceder a la documentación:**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📋 Funcionalidades

### Gestión de Usuarios
- ✅ Crear nuevos usuarios
- ✅ Obtener usuario por ID
- ✅ Listar todos los usuarios
- ✅ Actualizar información de usuario
- ✅ Validación de email único
- ✅ Validación de biografía (máximo 500 caracteres)

### Gustos Musicales
- ✅ Agregar gustos musicales a un usuario
- ✅ Obtener gustos musicales de un usuario
- ✅ Normalización automática de gustos (minúsculas, sin duplicados)

## 🔗 API Endpoints

### Usuarios
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/usuarios` | Listar todos los usuarios |
| `POST` | `/usuarios` | Crear nuevo usuario |
| `GET` | `/usuarios/{id}` | Obtener usuario por ID |
| `PUT` | `/usuarios/{id}` | Actualizar usuario |

### Gustos Musicales
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/usuarios/{id}/gustos-musicales` | Agregar gustos musicales |
| `GET` | `/usuarios/{id}/gustos-musicales` | Obtener gustos musicales |

### Sistema
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/health` | Verificar estado de la aplicación |

## 📊 Modelo de Datos

### Usuario
```json
{
  "id": 1,
  "nombre": "Juan",
  "apellido": "Pérez",
  "email": "juan.perez@email.com",
  "fecha_nacimiento": "1990-01-15",
  "biografia": "Descripción del usuario...",
  "provincia": "Buenos Aires",
  "localidad": "La Plata",
  "gustos_musicales": ["rock", "jazz", "clásica"]
}
```

## 🛠️ Tecnologías Utilizadas

- **FastAPI** 0.114.2 - Framework web moderno y rápido
- **Uvicorn** 0.30.6 - Servidor ASGI
- **Python** - Lenguaje de programación

## 📝 Notas de Desarrollo

- **Almacenamiento**: Los datos se almacenan en memoria (se pierden al reiniciar)
- **Validaciones**: Email único, biografía limitada a 500 caracteres
- **Normalización**: Los gustos musicales se normalizan automáticamente
- **Arquitectura**: Separación clara de responsabilidades entre capas

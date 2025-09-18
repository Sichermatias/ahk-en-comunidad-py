# MC - Mi Comunidad (FastAPI, versión simple)

## Estructura
- main.py -> inicializa FastAPI
- Routes/users.py -> endpoints de usuarios y gustos musicales
- Services/users_service.py -> lógica de negocio
- repository/users_repository.py -> almacenamiento en memoria

## Ejecutar
```bash
py -m pip install -r requirements.txt
py -m uvicorn main:app --reload
```

## Endpoints
- POST /usuarios
- GET /usuarios/{id}
- PUT /usuarios/{id}
- POST /usuarios/{id}/gustos-musicales
- GET /usuarios/{id}/gustos-musicales

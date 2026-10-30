from pydantic import BaseModel

class Estudiante(BaseModel):
    id: int
    nombre: str
    edad: int
    correo: str 

class EstudianteActulizar(BaseModel):
    nombre:str
    edad: int
    correo: str
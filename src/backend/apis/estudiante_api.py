from fastapi import APIRouter, HTTPException
from ..services.estudiante_service import EstudianteServicio
from ..schemas.estudiante import Estudiante, EstudianteActulizar

rutasEstudiante = APIRouter(prefix='/estudiantes', tags=['Estudiantes'])
estudianteServicio = EstudianteServicio()

@rutasEstudiante.post('/')
def guardarEstudiantes(estudianteNuevo: Estudiante):
    try:
        return estudianteServicio.guardarEstudiantes(estudianteNuevo)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER, detail=str(e))

@rutasEstudiante.get('/') 
def mostrarEstudiantes():
    return estudianteServicio.mostrarEstudiantes()

@rutasEstudiante.put('/{id}')
def actulizarEstudiantes(id:int, estudianteActualizar: EstudianteActulizar):
    try:
        return estudianteServicio.actulizarEstudiantes(id, estudianteActualizar)
    except Exception as e:
        raise  HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER, detail=str(e))
@rutasEstudiante.delete('/{id}')  
def eliminarEstudiante(id:int):
    try:
        return estudianteServicio.eliminarEstudiante(id)
    except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER, detail=str(e))
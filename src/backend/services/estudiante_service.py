from ..repositories.estudiante_repositorio import EstudianteRepositorio
from ..schemas.estudiante import Estudiante, EstudianteActulizar
class EstudianteServicio:

    def __init__(self):
        self.__estudianteRespositorio = EstudianteRepositorio()

    def guardarEstudiantes(self, estudianteNuevo: Estudiante):
        try:
            return self.__estudianteRespositorio.guardarEstudiantes(estudianteNuevo)
        except Exception as e:
              raise str(e)
        
    def mostrarEstudiantes(self):
            return self.__estudianteRespositorio.mostrarEstudiantes()
    
    def actulizarEstudiantes(self, id:int, estudianteActualizar: EstudianteActulizar):
        try:
            return self.__estudianteRespositorio.actulizarEstudiantes(id, estudianteActualizar)
        except Exception as e:
             raise str(e)
    
    def eliminarEstudiante(self, id:int):
        try:
            return self.__estudianteRespositorio.eliminarEstudiante(id)
        except Exception as e:
             raise str(e)
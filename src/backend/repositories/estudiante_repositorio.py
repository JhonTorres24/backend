from ..schemas.estudiante import Estudiante,EstudianteActulizar
class EstudianteRepositorio:

    def __init__(self):
        self.__listaEstudiantes:list[Estudiante] = []

    def guardarEstudiantes(self, estudianteNuevo: Estudiante):
        try:
            self.__listaEstudiantes.append(estudianteNuevo)
            return estudianteNuevo 
        except Exception as e:
            raise str(e)

    def mostrarEstudiantes(self):
        return self.__listaEstudiantes

    def actulizarEstudiantes(self, id: int, estudianteActulizar:EstudianteActulizar):
        try:
            for _, valor in enumerate(self.__listaEstudiantes):
                if valor.id == id:
                    valor.nombre = estudianteActulizar.nombre
                    valor.edad = estudianteActulizar.edad
                    valor.correo = estudianteActulizar.correo
                    return valor
            return None
        except Exception as e:
            raise str(e)
    

    def eliminarEstudiante(self, id:int):
        try:
            for indice, valor in enumerate(self.__listaEstudiantes):
                if valor.id == id:
                    self.__listaEstudiantes.pop(indice)
                    return id
                return None    
        except Exception as e:
            raise str(e)
        
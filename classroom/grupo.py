
from classroom.asignatura import Asignatura

class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            if (self._asignaturas is None):
                self._asignaturas = [Asignatura(x)]
            else:
                self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if(lista is None):
            if (self.listadoAlumnos is None):
                self.listadoAlumnos = [alumno]
            else:
                self.listadoAlumnos += [alumno]
        else:
            self.listadoAlumnos = lista + [alumno]

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        texto = "Grupo de estudiantes: "
        if self._grupo == "grupo ordinado":
            texto += "grupo predeterminado"
        else:
            texto += self._grupo
        return texto

# Esta clase guarda los datos de cada estudiante.
# No hereda de MatriculaGeneral porque representa una persona, no un tipo de calculo de matricula.

class Estudiante:
    def __init__(self, nombre, fuera_de_fecha=False,
                 indice_desaprobatorio=False, tiene_beca=False):
        # __init__ se ejecuta al crear el objeto.
        self.nombre = nombre
        self.fuera_de_fecha = fuera_de_fecha
        self.indice_desaprobatorio = indice_desaprobatorio
        self.tiene_beca = tiene_beca

    def mostrar_datos(self):
        print("Estudiante:", self.nombre)
        print("Fuera de fecha:", self.fuera_de_fecha)
        print("Indice desaprobatorio:", self.indice_desaprobatorio)
        print("Tiene beca:", self.tiene_beca)
# SUBCLASE: agrega S/ 15 por indice academico desaprobatorio.
from matricula_general import MatriculaGeneral


class MatriculaDesaprobado(MatriculaGeneral):
    def calcular_costo(self):
        # Primero obtenemos el monto del siguiente metodo del MRO.
        monto = super().calcular_costo()
        return monto + 15.0

# SUBCLASE: cobra un recargo de S/ 15 por matricula fuera de fecha.
from matricula_general import MatriculaGeneral


class MatriculaExtemporanea(MatriculaGeneral):
    def calcular_costo(self):
        # super() busca el siguiente calcular_costo() segun el MRO.
        monto = super().calcular_costo()
        return monto + 15.0

# SUBCLASE: aplica un descuento del 50 % al monto recibido.
from matricula_general import MatriculaGeneral


class MatriculaBeca(MatriculaGeneral):
    def calcular_costo(self):
        # No siempre llama directamente a MatriculaGeneral.
        # En herencia multiple, super() respeta el MRO del objeto.
        monto = super().calcular_costo()
        return monto / 2

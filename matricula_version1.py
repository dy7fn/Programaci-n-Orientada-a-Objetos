# PRIMER PROGRAMA: beca, desaprobado y extemporanea.
from matricula_beca import MatriculaBeca
from matricula_desaprobado import MatriculaDesaprobado
from matricula_extemporanea import MatriculaExtemporanea


class MatriculaVersion1(MatriculaBeca,
                        MatriculaDesaprobado,
                        MatriculaExtemporanea):
    # No necesitamos redefinir calcular_costo(): usa los heredados.
    pass

# Al retornar de super(): (60 + 15 + 15) / 2 = S/ 45.00

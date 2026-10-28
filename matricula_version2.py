# SEGUNDO PROGRAMA: desaprobado, extemporanea y beca.
from matricula_desaprobado import MatriculaDesaprobado
from matricula_extemporanea import MatriculaExtemporanea
from matricula_beca import MatriculaBeca


class MatriculaVersion2(MatriculaDesaprobado,
                        MatriculaExtemporanea,
                        MatriculaBeca):
    pass

# Al retornar de super(): (60 / 2) + 15 + 15 = S/ 60.00
# PRUEBAS AUTOMATICAS. No se necesita instalar bibliotecas.
# Para ejecutar: python -m unittest pruebas.py -v
import unittest

from matricula_general import MatriculaGeneral
from matricula_beca import MatriculaBeca
from matricula_version1 import MatriculaVersion1
from matricula_version2 import MatriculaVersion2
from estudiante import Estudiante
from sistema_matricula import SistemaMatricula


class PruebasMatricula(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaMatricula()
        self.estudiante = Estudiante("Estudiante de prueba", True, True, True)
        self.despues = ["extemporanea", "desaprobado", "beca"]
        self.antes = ["beca", "extemporanea", "desaprobado"]

    def test_costo_general(self):
        self.assertEqual(MatriculaGeneral().calcular_costo(), 60.0)

    def test_primera_version(self):
        self.assertEqual(MatriculaVersion1().calcular_costo(), 45.0)

    def test_segunda_version(self):
        self.assertEqual(MatriculaVersion2().calcular_costo(), 60.0)

    def test_beca_despues_de_recargos(self):
        monto, pasos = self.sistema.calcular_pago(self.estudiante, self.despues)
        self.assertEqual(monto, 45.0)
        self.assertEqual(len(pasos), 4)

    def test_beca_antes_de_recargos(self):
        monto, _ = self.sistema.calcular_pago(self.estudiante, self.antes)
        self.assertEqual(monto, 60.0)

    def test_sin_condiciones(self):
        normal = Estudiante("Sin condiciones")
        monto, _ = self.sistema.calcular_pago(normal, self.despues)
        self.assertEqual(monto, 60.0)

    def test_solo_beca(self):
        becario = Estudiante("Solo beca", tiene_beca=True)
        monto, _ = self.sistema.calcular_pago(becario, self.despues)
        self.assertEqual(monto, 30.0)

    def test_orden_invalido(self):
        with self.assertRaises(ValueError):
            self.sistema.calcular_pago(self.estudiante, ["beca", "beca", "desaprobado"])

    def test_herencia_general_primero_no_permitida(self):
        with self.assertRaises(TypeError):
            class MatriculaIncorrecta(MatriculaGeneral, MatriculaBeca):
                pass


if __name__ == "__main__":
    unittest.main()
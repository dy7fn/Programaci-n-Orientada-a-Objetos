# ARCHIVO PRINCIPAL: integra todas las clases del proyecto.
# Para ejecutar: python main.py  (o py main.py en Windows)
from matricula_version1 import MatriculaVersion1
from matricula_version2 import MatriculaVersion2
from estudiante import Estudiante
from sistema_matricula import SistemaMatricula


def mostrar_mro(tipo_matricula):
    # El MRO indica en que orden se buscan los metodos.
    print("MRO de", tipo_matricula.__name__)
    for clase in tipo_matricula.__mro__:
        if clase is not object:
            print("  ->", clase.__name__)


def mostrar_pago(estudiante, sistema, orden):
    print("\nEstudiante:", estudiante.nombre)
    print("Orden de reglas:", " -> ".join(orden))

    # La logica del calculo esta en SistemaMatricula.
    total, detalle = sistema.calcular_pago(estudiante, orden)

    # Aqui solo mostramos el proceso en pantalla.
    for descripcion, monto in detalle:
        print(f"  {descripcion}: S/ {monto:.2f}")
    print(f"  TOTAL: S/ {total:.2f}")
    return total


def main():
    print("=" * 52)
    print("SISTEMA DE MATRICULA UNSCH - SEMESTRE 2026-II")
    print("=" * 52)

    # 1. Reproducimos las dos versiones de herencia multiple.
    primera = MatriculaVersion1()
    segunda = MatriculaVersion2()
    pago_1 = primera.calcular_costo()
    pago_2 = segunda.calcular_costo()

    print("\n1) SISTEMA ORIGINAL")
    print(f"Version 1 (beca, desaprobado, extemporanea): S/ {pago_1:.2f}")
    print(f"Version 2 (desaprobado, extemporanea, beca): S/ {pago_2:.2f}")
    print(f"Diferencia entre versiones: S/ {abs(pago_1 - pago_2):.2f}")

    # El caso NO indica que version cobro a cada estudiante.
    mostrar_mro(MatriculaVersion1)
    mostrar_mro(MatriculaVersion2)

    # 2. Creamos los dos estudiantes mencionados en el caso.
    luis = Estudiante("Luis Huamani Cardenas", True, True, True)
    rosa = Estudiante("Rosa Ccahuana Prado", True, True, True)

    # 3. Usamos una politica comun para que ambos paguen igual.
    sistema = SistemaMatricula()
    orden_comun = ["extemporanea", "desaprobado", "beca"]

    print("\n2) SISTEMA CORREGIDO: BECA DESPUES DE LOS RECARGOS")
    mostrar_pago(luis, sistema, orden_comun)
    mostrar_pago(rosa, sistema, orden_comun)

    # 4. Ejemplo de una politica distinta y EXPLICITA.
    # Aqui la beca se aplica antes de sumar los recargos.
    orden_alternativo = ["beca", "extemporanea", "desaprobado"]
    print("\n3) EJEMPLO ALTERNATIVO: BECA ANTES DE LOS RECARGOS")
    mostrar_pago(luis, sistema, orden_alternativo)

    print("\nCONCLUSION: el sistema corregido usa el orden que se indique.")
    print("La universidad debe decidir cual politica corresponde aplicar.")


if __name__ == "__main__":
    main()
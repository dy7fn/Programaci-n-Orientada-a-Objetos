# SISTEMA CORREGIDO: el orden de las reglas se indica explicitamente.
# Asi evitamos que dependa del orden de herencia de Python.

class SistemaMatricula:
    def __init__(self):
        self.costo_base = 60.0
        self.recargo_fecha = 15.0
        self.recargo_indice = 15.0

    def calcular_pago(self, estudiante, orden):
        """Devuelve (total, detalle) siguiendo el orden seleccionado."""

        # El orden debe tener exactamente las tres reglas, sin repetirse.
        reglas_validas = {"extemporanea", "desaprobado", "beca"}
        if len(orden) != 3 or set(orden) != reglas_validas:
            raise ValueError("El orden debe incluir extemporanea, desaprobado y beca una vez")

        monto = self.costo_base
        detalle = [("Pago base", monto)]

        # Recorremos las reglas en el orden elegido para este estudiante.
        for regla in orden:
            if regla == "extemporanea" and estudiante.fuera_de_fecha:
                monto += self.recargo_fecha
                detalle.append(("Recargo por matricula fuera de fecha", monto))

            elif regla == "desaprobado" and estudiante.indice_desaprobatorio:
                monto += self.recargo_indice
                detalle.append(("Recargo por indice desaprobatorio", monto))

            elif regla == "beca" and estudiante.tiene_beca:
                monto /= 2
                detalle.append(("Descuento de beca (50 %)", monto))

        # Devolvemos datos; la presentacion se hace en main.py.
        return monto, detalle
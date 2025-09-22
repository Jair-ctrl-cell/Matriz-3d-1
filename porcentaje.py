# Función para calcular descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento sobre un monto total.

    Parámetros:
        monto_total (float): Monto total de la compra.
        porcentaje_descuento (float): Porcentaje de descuento (10% por defecto).

    Retorna:
        float: Monto del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Ejemplo 1: solo monto total (usa el descuento por defecto del 10%)
    monto1 = 100.0
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1
    print(f"Compra 1: Monto = ${monto1}, Descuento = ${descuento1}, Total a pagar = ${total1}")

    # Ejemplo 2: monto total y porcentaje de descuento especificado
    monto2 = 200.0
    porcentaje2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje2)
    total2 = monto2 - descuento2
    print(f"Compra 2: Monto = ${monto2}, Descuento = ${descuento2}, Total a pagar = ${total2}")

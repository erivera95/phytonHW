# Crea una función que valide los datos de una venta antes de procesarla.
# La función debe recibir un diccionario con "cliente", "monto" y "fecha".
# - Si el "monto" no es un número o es negativo, lanza una excepción ValueError.
# - Si la "fecha" no tiene el formato correcto (YYYY-MM-DD), lanza una excepción personalizada.
# - Si todo está correcto, retorna "Venta válida".

venta = {"cliente": "Juan", "monto": 1500, "fecha": "2024-01-02"}
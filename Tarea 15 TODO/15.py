# =========================================================
# 📌 Sistema de Gestión de Ventas - Ejercicio Integral
# =========================================================
# Este ejercicio combina listas, diccionarios, procesamiento de datos, control de flujo,
# funciones, excepciones, POO, manejo de archivos y conceptos avanzados de Python.
# Se recomienda abordarlo en partes, explicando cada sección por separado.

# =========================================================
# 1️⃣ Listas y Diccionarios: Definir productos y clientes
# =========================================================

# Diccionario de productos con su precio
productos = {
    "Laptop": 15000,
    "Mouse": 500,
    "Teclado": 1200,
    "Monitor": 4000,
    "Silla Gamer": 7000,
}

# Lista de clientes con información de compras
clientes = [
    {"nombre": "Juan", "compras": [("Laptop", 1), ("Mouse", 2)]},
    {"nombre": "Ana", "compras": [("Monitor", 1), ("Teclado", 1)]},
    {"nombre": "Luis", "compras": [("Silla Gamer", 1)]},
]

# =========================================================
# 2️⃣ Colección y Procesamiento de Datos en Python: Calcular totales
# =========================================================


def calcular_total_compras(clientes, productos):
    """
    Calcula el total gastado por cada cliente.
    """
    resumen = {}
    for cliente in clientes:
        total = sum(productos[item] * cantidad for item, cantidad in cliente["compras"])
        resumen[cliente["nombre"]] = total
    return resumen


# =========================================================
# 3️⃣ Control de Flujo en Python: Aplicar descuentos
# =========================================================


def aplicar_descuentos(resumen_compras):
    """
    Aplica un descuento del 10% si el cliente gastó más de $10,000.
    """
    for cliente, total in resumen_compras.items():
        if total > 10000:
            resumen_compras[cliente] *= 0.9  # Aplica 10% de descuento
    return resumen_compras


# =========================================================
# 4️⃣ Funciones y Manejo de Excepciones: Realizar una compra segura
# =========================================================


def realizar_compra(cliente, producto, cantidad):
    """
    Añade un producto a la compra de un cliente, manejando excepciones.
    """
    try:
        if producto not in productos:
            raise ValueError("El producto no existe en el catálogo.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")

        # Agregar compra al cliente
        for c in clientes:
            if c["nombre"] == cliente:
                c["compras"].append((producto, cantidad))
                return f"✅ {cliente} compró {cantidad} unidad(es) de {producto}."

        return "❌ Cliente no encontrado."
    except ValueError as e:
        return f"⚠️ Error: {e}"


# =========================================================
# 5️⃣ Programación Orientada a Objetos: Reportes de Ventas
# =========================================================


class ReporteVentas:
    def __init__(self, clientes, productos):
        """
        Inicializa el reporte con los datos de clientes y productos.
        """
        self.clientes = clientes
        self.productos = productos

    def generar_reporte(self):
        """
        Muestra el total de ventas por cliente.
        """
        resumen = calcular_total_compras(self.clientes, self.productos)
        resumen = aplicar_descuentos(resumen)

        reporte = "\n📊 Reporte de Ventas:\n"
        for cliente, total in resumen.items():
            reporte += f"   - {cliente}: ${total:.2f}\n"
        return reporte


# =========================================================
# 6️⃣ Lectura y Escritura de Archivos: Guardar reporte en un archivo
# =========================================================


def guardar_reporte(reporte, nombre_archivo="reporte_ventas.txt"):
    """
    Guarda el reporte de ventas en un archivo de texto.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as file:
        file.write(reporte)
    return f"📂 Reporte guardado en {nombre_archivo}"


# =========================================================
# 7️⃣ Conceptos Avanzados de Python: Expresiones Lambda y Dict Comprehension
# =========================================================

# Generar un resumen de ventas usando comprensión de diccionario
resumen_ventas = {
    cliente["nombre"]: sum(
        productos[item] * cantidad for item, cantidad in cliente["compras"]
    )
    for cliente in clientes
}

# Aplicar un descuento del 10% usando lambda si el total es mayor a 10,000
resumen_ventas = {
    cliente: (lambda total: total * 0.9 if total > 10000 else total)(total)
    for cliente, total in resumen_ventas.items()
}


# =========================================================
# 🔹 Pruebas del Sistema
# =========================================================

# Calcular totales
resumen = calcular_total_compras(clientes, productos)
print("🛒 Resumen de Compras:", resumen)

# Aplicar descuentos
resumen_con_descuentos = aplicar_descuentos(resumen)
print("💰 Resumen con Descuentos:", resumen_con_descuentos)

# Realizar una compra segura
print(realizar_compra("Juan", "Teclado", 1))
print(realizar_compra("Ana", "Mouse", -1))  # Error

# Generar y guardar el reporte de ventas
reporte = ReporteVentas(clientes, productos).generar_reporte()
print(reporte)
print(guardar_reporte(reporte))

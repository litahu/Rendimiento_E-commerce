"""Visor de documentación para Tienda Aurelion (con contenido incrustado).

Este script implementa un menú de consola simple que imprime las secciones
definidas en `documentacion.md`. Las secciones están copiadas directamente en
variables para cumplir la instrucción de contener la misma información dentro
del archivo.

Reglas aplicadas:
- Bucle principal que muestra el menú y permite volver hasta elegir Salir.
- Funciones sencillas por sección: `mostrar_tema()`, `mostrar_metadatos()`, etc.
"""

from typing import Callable


def mostrar_tema() -> None:
    print("\n=== 1. Tema, problema y objetivo ===\n")
    print("Tema: Análisis del comportamiento de los clientes")
    print()
    print("Problema: Se sospecha que existen inconsistencias en el comportamiento de compra de los clientes en temporadas del año, dado que los costes operativos se han elevado por la poca rotación de productos.")
    print()
    print("Solución: Se va a realizar un análisis de serie de tiempo en ventas")
    print("\n---\n")


def mostrar_metadatos() -> None:
    print("\n=== 2. Metadatos del dataset de referencia ===\n")
    print("A continuación se proponen tablas de metadatos para cada archivo Excel: Clientes.xlsx, Detalle_ventas.xlsx, Productos.xlsx y Ventas.xlsx\n")
    print("--- Clientes ---")
    print("ID_Cliente: Int, Cuantitativo, Discreto")
    print("Nombre_Cliente: Str, Cualitativo, Nominal")
    print("Email: Str, Cualitativo, Nominal")
    print("Ciudad: Str, Cualitativo, Nominal")
    print("Fecha_alta: DateTime, Cuantitativo, Intervalo")
    print()
    print("--- Productos ---")
    print("ID_producto: Int, Cuantitativo, Discreto")
    print("nombre_producto: Str, Cualitativo, Nominal")
    print("categoria: Str, Cualitativo, Nominal")
    print("precio_unitario: Float, Cuantitativo, Continuo")
    print()
    print("--- Ventas ---")
    print("ID_venta: Int, Cuantitativo, Discreto")
    print("fecha: DateTime, Cuantitativo, Intervalo")
    print("ID_cliente: Int, Cuantitativo, Discreto")
    print("nombre_cliente: Str, Cualitativo, Nominal")
    print("email: Str, Cualitativo, Nominal")
    print("medio_pago: Str, Cualitativo, Nominal")
    print()
    print("--- Detalle_ventas ---")
    print("ID_Venta: Int, Cuantitativo, Discreto (FK)")
    print("ID_Producto: Int, Cuantitativo, Discreto (FK)")
    print("nombre_producto: Str, Cualitativo, Nominal")
    print("cantidad: Int, Cuantitativo, Discreto")
    print("precio_unitario: Float, Cuantitativo, Continuo")
    print("importe: Float, Cuantitativo, Continuo")
    print("\n---\n")


def mostrar_relaciones() -> None:
    print("\n=== 3. Relación de entidades ===\n")
    print("Relaciones esperadas entre tablas:\n")
    print("- Clientes (PK: ID Cliente)")
    print("- Productos (PK: ID Producto)")
    print("- Ventas (PK: ID Venta, FK: ID Cliente -> Clientes.ID Cliente)")
    print("- Detalle_ventas (PK: ID Venta -> Ventas.ID Venta, FK: ID Producto -> Productos.ID Producto)")
    print("\nEjemplo en texto:\nClientes.ID Cliente (1) <--- (N) Ventas.ID Cliente\nVentas.ID Venta (1) <--- (N) Detalle_ventas.ID Venta\nProductos.ID Producto (1) <--- (N) Detalle_ventas.ID Producto")
    print("\n---\n")


def mostrar_diagrama() -> None:
    print("\n=== 4. Diagrama del programa (pseudocódigo) ===\n")
    print("Inicio")
    print("  Cargar texto de documentación desde 'documentacion.md' a memoria (o incrustar directamente en variables)")
    print("  Mientras True:")
    print("    Mostrar menú principal con opciones numeradas (1..6)")
    print("    Leer opción del usuario")
    print("    Si opción == 1: mostrar sección 'Tema, problema y solución'")
    print("    Si opción == 2: mostrar sección 'Metadatos del dataset de referencia'")
    print("    Si opción == 3: mostrar sección 'Relación de entidades'")
    print("    Si opción == 4: mostrar sección 'Diagrama del programa'")
    print("    Si opción == 5: mostrar sección 'Sugerencias y mejoras con Copilot'")
    print("    Si opción == 6: salir del programa")
    print("    Si entrada inválida: mostrar mensaje de error y volver a mostrar menú")
    print("  FinMientras")
    print("Fin")
    print("\n---\n")


def mostrar_sugerencias() -> None:
    print("\n=== 5. Sugerencias y mejoras con Copilot ===\n")
    print("- Añadir validaciones de esquema cuando se carguen los archivos .xlsx (columnas obligatorias, tipos, no-negatividad de precios y cantidades).")
    print("- Implementar tests unitarios para las funciones que parsean y validan metadatos.")
    print("- Añadir una opción en la GUI para exportar la documentación a PDF usando reportlab o weasyprint.")
    print("- Añadir una página de resumen con KPIs (ventas totales, clientes activos, top 10 productos) que se actualice al cargar los datos reales.")
    print("- Manejar localizaciones/fechas con dateutil y normalizar los formatos de fecha.")
    print("\n---\n")


def mostrar_menu() -> None:
    opciones = [
        "1. Tema, problema y solución",
        "2. Metadatos del dataset de referencia",
        "3. Relación de entidades",
        "4. Diagrama del programa",
        "5. Sugerencias y mejoras con Copilot",
        "6. Salir",
    ]
    print("\nVisor de Documentación - Tienda Aurelion")
    for opt in opciones:
        print(opt)


def main() -> None:
    acciones: dict[str, Callable[[], None]] = {
        "1": mostrar_tema,
        "2": mostrar_metadatos,
        "3": mostrar_relaciones,
        "4": mostrar_diagrama,
        "5": mostrar_sugerencias,
    }

    while True:
        mostrar_menu()
        try:
            elec = input("Selecciona una opción (1-6): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo...")
            break

        if elec == "6":
            print("Adiós")
            break
        if elec in acciones:
            acciones[elec]()
            input("Presiona Enter para volver al menú...")
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()

# Proyecto Tienda Aurelion


## 1. Tema, problema y objetivo

Tema: Análisis del comportamiento de los clientes

Problema: Se sospecha que existen inconsistencias en el comportamiento de compra de los clientes en temporadas del año, dado que los costes operativos se han elevado por la poca rotación de productos. 

Solución: Se va a realizar un análisis de serie de tiempo en ventas


## 2. Metadatos del dataset de referencia

A continuación se proponen tablas de metadatos para cada archivo Excel: Clientes.xlsx, Detalle_ventas.xlsx, Productos.xlsx y Ventas.xlsx


### Clientes

|  Variable      |   Estructura      | Tipo de Dato |  
|----------------|-------------------|--------------|  
| ID_Cliente     | Int, Cuantitativo | Discreto     |
| Nombre_Cliente | Str, Cualitativo  | Nominal      |
| Email          | Str, Cualitativo  | Nominal      |
| Ciudad         | Str, Cualitativo  | Nominal      | 
| Fecha_alta     | DateTime, Cuantitativo | Intervalo |  

Descripción: `ID Cliente` es la clave primaria; `Email` y `Teléfono` pueden contener nulos.- Clientes (Clientes.xlsx)


### Productos

|   Estructura   | Tipo de Dato      |   Escala  |
|----------------|-------------------|-----------|
| ID_producto    | Int, Cuantitativo | Discreto  |
| nombre_producto| Str, Cualitativo  | Nominal   |
| categoria      | Str, Cualitativo  | Nominal   |
| precio_unitario| Float, Cuantitativo| Continuo |

Descripción: `ID Producto` es la clave primaria; `Precio Unitario` y `Stock` deben validarse para valores negativos.- Ventas.VentaID -> PK


### Ventas

|   Estructura   | Tipo de Dato |   Escala  |
|----------------|--------------|-----------|
| ID_venta       | Int, Cuantitativo | Discreto |
| fecha          | DateTime, Cuantitativo | Intervalo |
| ID_cliente     | Int, Cuantitativo | Discreto |
| nombre_cliente | Str, Cualitativo | Nominal |
| email          | Str, Cualitativo | Nominal |
| medio_pago     | Str, Cualitativo | Nominal |

Descripción: `ID Venta` es la clave primaria; `ID Cliente` referencia a `Clientes.ID Cliente`


### Detalle_ventas  

|   Estructura     | Tipo de Dato |   Escala  | 
|------------------|--------------|-----------|
| ID_Venta         | Int, Cuantitativo | Discreto (FK) |
| ID_Producto      | Int, Cuantitativo | Discreto (FK) |
| nombre_producto  |  Str, Cualitativo | Nominal  |
| cantidad         | Int, Cuantitativo | Discreto |
| precio_unitario  | Float, Cuantitativo| Continuo |
| importe          | Float, Cuantitativo| Continuo |


Descripción: `ID Venta` referencia a `Ventas.ID Venta`; `ID Producto` referencia a `Productos.ID Producto`.- cargar_documentacion(ruta) -> dict[num_opcion] = texto



## 3. Relación de entidades

Relaciones esperadas entre tablas:

- `Clientes` (PK: `ID Cliente`)

- `Productos` (PK: `ID Producto`)

- `Ventas` (PK: `ID Venta`, FK: `ID Cliente` -> `Clientes.ID Cliente`)

- `Detalle_ventas` (PK: `ID Venta` -> `Ventas.ID Venta`, FK: `ID Producto` -> `Productos.ID Producto`)



## 4. Diagrama del programa (pseudocódigo)

El visor interactivo (archivo `programa.py`) seguirá este pseudocódigo:

- Requisitos (sugeridos):
  - Python 3.8+

```  
Inicio  - openpyxl (si se quieren leer los .xlsx desde Python)

  Cargar texto de documentación desde `documentacion.md` a memoria (o incrustar directamente en variables)  - matplotlib (opcional, para gráficos)

  Mientras True:

    Mostrar menú principal con opciones numeradas (1.6). Ejemplo rápido desde consola:

    Leer opción del usuario

    Si opción == 1: mostrar sección "Tema, problema y solución"python programa.py

    Si opción == 2: mostrar sección "Metadatos del dataset de referencia"

    Si opción == 3: mostrar sección "Relación de entidades"Y para la interfaz gráfica:

    Si opción == 4: mostrar sección "Diagrama del programa"

    Si opción == 5: mostrar sección "Sugerencias y mejoras con Copilot"python grafico.py

    Si opción == 6: salir del programa

    Si entrada inválida: mostrar mensaje de error y volver a mostrar menú

  FinMientras

Fin## Notas finales

```

Actualiza las secciones de metadatos cuando tengas los archivos Excel reales: `Clientes.xlsx`, `Detalle_ventas.xlsx`, `Productos.xlsx`, `Ventas.xlsx`.

Implementación sugerida: encapsular cada opción en una función pequeña (`mostrar_tema()`, `mostrar_metadatos()`, ...) para facilitar pruebas y posible reutilización desde la GUI.



## 5. Sugerencias y mejoras con Copilot
- Añadir validaciones de esquema cuando se carguen los archivos `.xlsx` (columnas obligatorias, tipos, no-negatividad de precios y cantidades).
- Implementar tests unitarios para las funciones que parsean y validan metadatos.
- Añadir una opción en la GUI para exportar la documentación a PDF usando `reportlab` o `weasyprint`.
- Añadir una página de resumen con KPIs (ventas totales, clientes activos, top 10 productos) que se actualice al cargar los datos reales.
- Manejar localizaciones/fechas con `dateutil` y normalizar los formatos de fecha.

#### Dependencias y cómo ejecutar
Requisitos mínimos:
- Python 3.8+
- Paquetes (recomendados): `pandas`, `openpyxl`, `matplotlib` (opcional para gráficos)
- `tkinter` (incluido en la mayoría de distribuciones de Python en Windows)

Instalación rápida (PowerShell):
```powershell
python -m pip install --upgrade pip; python -m pip install pandas openpyxl matplotlib
```

Ejecutar el visor de consola:
```powershell
python .\programa.py
```

Ejecutar la interfaz gráfica (cuando exista):
```powershell
python .\grafico.py
```


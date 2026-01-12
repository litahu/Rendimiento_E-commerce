"""
Proyecto Aurelion

1. Problema que quiero resolver
El objetivo de este proyecto es organizar y analizar la información de ventas, clientes y productos dentro de una base de datos.
Con esta estructura se busca responder preguntas como:

- ¿Qué productos se venden más y cuáles menos?
- ¿Qué medios de pago usan los clientes con mayor frecuencia?
- ¿Existen patrones de consumo según la ciudad o la fecha?
- ¿Qué clientes son los más activos en términos de compras?

La finalidad es generar reportes claros y fáciles de interpretar para la toma de decisiones comerciales.

2. Estructura de la base de datos
La base de datos se compone de cuatro tablas principales:

Ventas
- id_venta (PK)
- fecha
- id_cliente (FK → Clientes.id_cliente)
- medio_pago

Detalle de ventas
- id_venta (FK → Ventas.id_venta)
- id_producto (FK → Productos.id_producto)
- cantidad
- precio_unitario
- importe

Productos
- id_producto (PK)
- nombre_producto
- categoria
- precio_unitario

Clientes
- id_cliente (PK)
- nombre_cliente
- email
- ciudad
- fecha_alta

3. Tipos de datos
- id_venta, id_cliente, id_producto: int
- fecha, fecha_alta: date
- nombre_cliente, email, ciudad, nombre_producto, categoria, medio_pago: string
- precio_unitario, importe: float
- cantidad: int

4. Escala esperada
- Ventas: desde decenas hasta miles de registros dependiendo del periodo analizado.
- Clientes: crecerá gradualmente conforme se registren nuevos clientes.
- Productos: lista relativamente estable, con decenas o cientos de referencias.
- Detalle de ventas: será la tabla más grande, ya que cada venta puede incluir varios productos.
"""
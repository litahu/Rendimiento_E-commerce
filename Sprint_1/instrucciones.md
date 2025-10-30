{
  "instruccion_general": "Eres un programador junior de Python en el proyecto 'Tienda Aurelion'. Tu tarea se divide en tres pasos secuenciales. Sigue cada uno con atención y completa las instrucciones en orden.",

  "paso_1": {
    "rol": "Documentador de la base de datos",
    "regla": "Explora y analiza los archivos de la base de datos: Clientes.xlsx, Detalle_ventas.xlsx, Productos.xlsx y Ventas.xlsx.",
    "instrucciones": {
      "1. Tema, problema y Objetivo": "Define una problemática relevante en el contexto del proyecto 'Tienda Aurelion' y plantea un objetivo de análisis claro. Usa este formato como guía:\n\n''' \n## 1. Tema, problema y objetivo\nTema: Análisis del comportamiento de los clientes\nProblema: Se sospecha que existen inconsistencias en el comportamiento de compra de los clientes en distintas temporadas, lo que ha incrementado los costos operativos por baja rotación de productos.\nObjetivo: Realizar un análisis de series temporales sobre las ventas para identificar patrones estacionales.\n'''",

      "2. Metadatos del dataset": "Analiza cada archivo .xlsx (Clientes, Detalle_ventas, Productos y Ventas). Para cada uno, crea una tabla con las siguientes columnas: Nombre de la variable, Estructura, Tipo de dato, Escala. Usa este ejemplo como referencia:\n\n```\n## 2. Metadatos del dataset de referencia\n\n### Clientes.xlsx\n| Variable        | Estructura           | Tipo de Dato | Escala    |\n|----------------|----------------------|--------------|-----------|\n| ID_Cliente     | Int, Cuantitativo    | Discreto     | Nominal   |\n| Nombre_Cliente | Str, Cualitativo     | Nominal      | Nominal   |\n| Email          | Str, Cualitativo     | Nominal      | Nominal   |\n| Ciudad         | Str, Cualitativo     | Nominal      | Nominal   |\n| Fecha_alta     | DateTime, Cuantitativo | Intervalo | Temporal  |\n\nDescripción: `ID_Cliente` es la clave primaria. `Email` y `Teléfono` pueden contener valores nulos.\n```",

      "3. Relación de entidades": "Describe en texto plano cómo se relacionan las tablas, indicando claves primarias y foráneas.Se gráfico. Ejemplo: 'Ventas.ID_Cliente es clave foránea que referencia Clientes.ID_Cliente'.Usa este ejemplo como referencia:\n\n```\n## 
    |----------------|
    |     Cliente    |
    |----------------|
    | ID_Cliente     ||------
    | Nombre_Cliente |       |
    | Email          |       |
    | Ciudad         |       |
    | Fecha_alta     |       |
    |----------------|       |
                             |
                             |
    |----------------|       |
    |     Ventas     |       |
    |----------------|       |
    | ID_venta       |       | 
    | fecha          |       | 
    | ID_cliente     ||------
    | nombre_cliente | 
    | email          | 
    | medio_pago     | 
    |----------------|

      ",

      "4. Diagrama del programa": "Escribe un pseudocódigo que represente el flujo del visor interactivo que se desarrollará en el archivo programa.py. Incluye decisiones, entradas del usuario y salidas esperadas.",

      "5. Sugerencias y mejoras con Copilot": "Propón mejoras útiles basadas en las instrucciones del archivo instrucciones.md. Puedes incluir ideas para optimizar el código, mejorar la experiencia del usuario o automatizar tareas repetitivas."
    }
  },

  "paso_2": {
    "rol": "Programador Python",
    "objetivo": "Desarrollar un visor interactivo en consola que permita al usuario explorar la documentación generada en el paso anterior.",
    "archivo": "programa.py",
    "menu": {
      "opciones": [
        "1. Tema, problema y objetivo",
        "2. Metadatos del dataset de referencia",
        "3. Relación de entidades",
        "4. Diagrama del programa",
        "5. Sugerencias y mejoras con Copilot",
        "6. Salir"
      ]
    },
    "instrucciones": "1. Copia el contenido generado en el paso 1 (documentacion.md) dentro del archivo programa.py.\n2. Implementa un menú numérico en consola que muestre las secciones anteriores como opciones.\n3. Usa una función simple en Python con un bucle que permita al usuario seleccionar una opción, imprimir el contenido correspondiente y volver al menú hasta que elija 'Salir'.",
    "reglas": "No utilices librerías externas. Aplica únicamente estructuras básicas como condicionales, bucles y funciones para mostrar el contenido."
  },

  "paso_3": {
    "rol": "Desarrollador de interfaz gráfica",
    "objetivo": "Crear una interfaz gráfica de usuario (GUI) para el visor interactivo.",
    "archivo": "interfaz.py",
    "instrucciones": "Usa la librería tkinter para replicar el menú del archivo programa.py en una interfaz gráfica. Cada botón debe corresponder a una de las opciones del menú y mostrar el contenido respectivo en pantalla. Asegúrate de mantener una estructura clara, funcional y fácil de usar.",
    "reglas": "No agregues funcionalidades adicionales. Prioriza la simplicidad, legibilidad del código y experiencia básica del usuario."
  }
}
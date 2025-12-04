{
  "instruccion_general": "Eres un programador junior de Python en el proyecto 'Tienda Aurelion'. Sigue todos los pasos en orden.",
  
  "paso_1": {
    "rol": "Documentador de la base de datos",
    "Regla": "Explora la base de datos compuesta por los archivos: Clientes.xlsx, Detalle_ventas.xlsx, Productos.xlsx y Ventas.xlsx",
    "Instruccion": {
      "1.Tema, problema y una solución": "Define con claridad una problemática de las ventas en el conteto del proyecto Aurelion para palntear un objetivo de analisis. Guiate de este ejemplo:
      '''
      ## 1. Tema, problema y objetivo
      Tema: Análisis del comportamiento de los clientes
      Problema: Se sospecha que existen inconsistencias en el comportamiento de compra de los clientes en temporadas del año, dado que los costes operativos se han elevado por la poca rotación de productos. 
      Solución: Se va a realizar un análisis de serie de tiempo en ventas
      '''
      ",
      "2.Metadatos del dataset": "*Analiza cada archivo .xlsx proporcionado: Clientes.xlsx, Detalle_ventas.xlsx, Productos.xlsx y Ventas.xlsx. Identifica el nombre de la variable, su estructura, tipo de dato y la escala de cada variable por cada tabla que realices del archivo.xlxs
      Seguí el siguiente ejemplo:
    
      ```
     ## 2. Metadatos del dataset de referencia
     A continuación se proponen tablas de metadatos para cada archivo Excel: Clientes.xlsx, Detalle_ventas.xlsx, Productos.xlsx y Ventas.xlsx
     
     ### Clientes
     |  Variable      |   Estructura      | Tipo de Dato |  
     |----------------|-------------------|--------------|  
     | ID_Cliente     | Int, Cuantitativo | Discreto     |
     | Nombre_Cliente | Str, Cualitativo  | Nominal      |
     | Email          | Str, Cualitativo  | Nominal      |
     | Ciudad         | Str, Cualitativo  | Nominal      | 
     | Fecha_alta     | DateTime, Cuantitativo | Intervalo |  
     Descripción: `ID Cliente` es la clave primaria; `Email` y `Teléfono` pueden contener nulos.- Clientes (Clientes.xlsx)
     
      ```
     ",
      "3.Relación de entidades": "Diagrama la relación entre las tablas en texto plano, indicando la relacion según su clave primaria y foránea",
      "4.Diagrama del programa": "Diagrama en pseudocódigo el flujo del visor interactivo que se desarrollará en el archivo programa.py.",
      "5.Sugerencias y mejoras con Copilot": "Sugiere mejoras útiles vinculado a las instrucciones que te brindo en el archivo instrucciones.md"
    }
  },
  "paso_2": {
    "rol": "Programador Python",
    "objetivo": "Desarrolla un visor interactivo en consola que permita al usuario acceder a la misma informacion contenida en archivo documentacion.md desde un menú. Imprime el contenido correspondiente en pantalla y permite volver al menú principal hasta que el usuario seleccione 'Salir'.",
    "archivo": "programa.py",
    "menu": {
      "opciones": [
        "1. Tema, problema y solución",
        "2. Metadatos del dataset de referencia",
        "3. Relación de entidades",
        "4. Diagrama del programa",
        "5. Sugerencias y mejoras con Copilot",
        "6. Salir"
      ]
    },
    "instruccion": "
    1. Copia la información que se detalla en la documentacion.md dentro de este archivo. A partir de ahi convierte los apartados de los  titulos en condiciones a imprimir dentro de un menu. 
    2. Muestra un menú numérico con una función simple en python que itere los titulos de las instrucciones. Recuerda que son estos: [
        "1. Tema, problema y solución",
        "2. Metadatos del dataset de referencia",
        "3. Relación de entidades",
        "4. Diagrama del programa",
        "5. Sugerencias y mejoras con Copilot"] ",
    
    "Reglas": " Solo aplica una función básica como un bucle que va a ir imprimiendo los cotenidos al invocar el apartado de cada titulo. Ademas iteras dentro del menu y te da la opcion de salir"
  },
  "paso_3": {
    "objetivo": "Aplicación gráfica de interfaz de usuario",
    "instruccion": "Vas a utilizar la librería tkinter para crear una interfaz gráfica al menú que se aplicaba en el archivo[programa.py]. Implementa este visor dentro de un archivo llamado interfaz.py. Recuerda que Los botones deben ser los mismos que se aplicaban en el menú y ademas debe imprimir el mismo contenido. Se busca uan interfaz para el usuario. Procura mantener funcionalidad basicas y eficaces"
  }
}


# 💰 **Análisis del rendimiento de un E-commerce**
<img src="https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_1/IMAGES/LOGO_END.png?raw=true" alt="inserir alt">
<br>

**Tool** : [Notebook](https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_2/Aurelion_2.ipynb)<br>
**Visualización** : Aplicación desarrollada en **Python + Streamlit** <br>
**Dataset** : [Ecommerce Data](https://github.com/litahu/Rendimiento_E-commerce/tree/main/Sprint_1/BD)<br>
<br>
<br>

---

## 📁**ETAPA 0: Enunciado del problema**

### **Historia de fondo**

Tienda Aurelión es una gran minorista que atiende algunas provincias de Córdova a través de su e-commerce. Es conocida por la amplia variedad de productos que ofrece, buscando satisfacer a todo tipo de público desde sus centros de distribución (CDs).

La tienda Aurelión atraviesa una situación crítica y necesita tu apoyo para mantenerse operativa. En los últimos meses, ha experimentado un estancamiento en su flujo de caja. Para contribuir a la toma de decisiones estratégicas en su plataforma online, se te proporciona acceso a cuatro bases de datos: clientes, detalle de ventas, productos y ventas.

### **Objetivo**
Recopilar información a partir de análisis y visualizaciones en forma de:

1. **Crecimiento mensual de la actividad del cliente**
2. **Calidad mensual de la categoría de productos**
3. **Uso del tipo de pago mensual**

<br>
<br>

---
## 📁**ETAPA 1: Preparación de datos**
El conjunto de datos utilizado pertenece a Tienda Aurelión y contiene información de pedidos, con un total de 336 registros realizados en el primer semestre del 2023. Se incluye características que generan información como el estado del pedido, la ubicación, el tipo de pago y las reseñas por valor.

### **Crear base de datos y diagrama ER**

**Las medidas adoptadas incluyen:**
1. Crea un espacio de trabajo de base de datos
2. Importar datos CSV a la base de datos
3. Determinar la clave primaria o la clave foránea
4. Crear y exportar diagramas ERD (diagramas de entidad-relación).

**Resultados de ERD:**<br>
<p align= "center">
  <kbd><img src="https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_1/IMAGES/DRE.png" width=600px> </kbd> <br>
  Figura 1. Diagrama de relación de entidades
</p>  


<br>
<br>

---

## 📂 **ETAPA 2: Análisis de datos**

### **1. Comportamiento del cliente**

Las formas de compras pueden analizarse por los productos que adquieren. En general, la empresa ha experimentado un aumento en el número de compras de la categoría: abarrotes, limpieza, embutidos, bebidas cada año.
<p align= "center">
  <kbd><img src="https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_2/assets/plan_alto.png" width=600px> </kbd> <br>
</p>  
<p align= "center">
  <kbd><img src="https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_2/assets/plan_medio.png" width=600px> </kbd> <br>
</p> 
<p align= "center">
  <kbd><img src="https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_2/assets/plan_bajo.png" width=600px> </kbd> <br>
</p> 

### **2. Calidad de la categoría de productos**

La empresa generó los mayores ingresos con su categoría de productos Abarrotes y limpieza. Sin embargo, las bebidas y embutidos tienen a ser categorías líder en diferente meses festivos.

<p align= "center">
  <kbd><img src="https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_2/assets/ventas_mensuales.png" width=600px> </kbd> <br>
  Figura 2. Gráfico de las ventas de las categorías top
<br>
</p>  


### **3. Uso del tipo de pago**

La mayoría de los clientes realizan sus pagos con "QR", y esta cifra tiende a aumentar cada mes. Los pagos en "efectivo" aumentaron los dos últimos meses a pesar que venía disminuyendo en abril. Por otro lado la "tarjeta(de débito, de crédito)" y las "transferencias" tienen una tendencia de uso bajista. Esto se debe probablemente a las altas comisiones que se cobran por costos de cobro que se transfieren al consumidor.

<p align= "center">
  <kbd><img src="https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_2/assets/medio_pago.png" width=600px> </kbd> <br>
  Figura 3. Gráfico del tipo de pago favoritos
</p>  

<br>
<br>

---

## 📂 **ETAPA 3: Resumen**

- Según el comportamiento de los clientes, se puede concluir que suelen adquirir entre 2, 3 y 4 productos.
Los clientes con un plan de consumo de medio a alto residen en Alta Gracia y Río Cuarto. Mientras, que los clientes más críticos residen en Mendiolaza y Villa María.
Por lo tanto, se necesita una estrategia comercial para aumentar el interés de los clientes con llamadas a la acción de acuerdo al perfil del cliente

- Según el análisis las categorías consumidas por los clientes con un "Plan alto" es **Embutidos**, **abarrotes** y **bebidas**, mientras que los clientes con un "Plan Medio" son **Abarrotes**, **embutidos** y **limpieza** y finalmente, los clientes con un "Plan Bajo" solo se sostiene para la categoría abarrrotes **Abarrotes**. A partir de este análisis, se puede desarrollar una estrategia comercial que incluya promociones entre estas categorías segun el perfil de consumo, lo que se espera que incremente las oportunidades de generación de ingresos de la empresa.

- Las pagos con QR y en efectivo son los tipo de pago favoritos de los clientes. Se invita colocar promociones para incentivar estos tipos de pago. Cabe resaltar que los consumidores no desean asumir las comisiones de las transferencias y tarjetas(de crédito, de depósito).

<br>
<br>

---
## 📂 **ETAPA 4: Presentación**

<p align="center">
  <a href="https://drive.google.com/file/d/1-epThm9diWGVSOsFJq6HmCeT-WlxyZAi" style="font-size:18px; font-weight:bold;">🔗 Ver demo</a>
</p>

<p align= "center">
  <kbd><img src="https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_2/assets/demoSprint2.PNG" width=600px> </kbd> <br>
</p>  

<p align="center">
  <a href="https://drive.google.com/file/d/1-epThm9diWGVSOsFJq6HmCeT-WlxyZAi" style="font-size:18px; font-weight:bold;">🔗 Ver demo</a>
</p>
































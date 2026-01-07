
# 💰 **Panel de Control de la Tienda aurelión**

**Tool** : [Mokkup](https://www.mokkup.ai/) <br>
**Visualización** : Power BI(ETL, Power Query, DAX y plugins) <br>
**Dataset** : [Ecommerce Data](https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_3/bd_venta_aurelion.xlsx)<br>
<br>
<br>

---
## 📁**ETAPA 0: Plan de modelado y diseño**
Enfocado en el contexto de negocio, se diseñó un wireframe del panel con el objetivo de optimizar la lógica de usabilidad para el usuario final. Este prototipo funciona como una guía visual para validar la disposición de los elementos, la jerarquía de la información y la interacción prevista dentro de la visualizacion en Power BI.

### **🔑 Objetos principales del Diseño UX/UI**:
- **Wireframes**
Bocetos estructurales que muestran la disposición de los elementos en pantalla sin entrar en detalles visuales. Sirven para validar la lógica de navegación y jerarquía de información.
- **Mockups**
Representaciones visuales más detalladas que incluyen colores, tipografías y estilos gráficos. Son útiles para comunicar la estética final de la interfaz.
- **Prototipos interactivos**
Versiones funcionales (aunque no definitivas) que permiten simular la interacción del usuario con la interfaz. Se usan para pruebas de usabilidad.
- **Componentes UI**
Elementos reutilizables como botones, menús, formularios, tarjetas, iconos y sliders. Facilitan consistencia y escalabilidad en el diseño.
- **Sistemas de diseño** (Design Systems)
Conjuntos de guías, librerías y patrones que aseguran coherencia visual y funcional en todos los productos digitales de una organización.
- **Flujos de usuario** (User Flows)
Diagramas que representan los pasos que sigue un usuario para completar una tarea dentro de la aplicación o sistema.
- **Personas y escenarios**
Representaciones ficticias de usuarios tipo que ayudan a diseñar pensando en necesidades reales y contextos específicos.

<br>

**Maquetación:**<br>
<p align= "center">
  <kbd><img src="https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_4/Resource/prototype.PNG " width=900px> </kbd> <br>
  Figura 1. Personalización de Objetos
</p>  

<br>
<br>

---
## 📁**ETAPA 1: Gráfico Visual de datos**
Acontinuación se integro los objetos de acuerdo a la usabilidad del cliente y a la optimizacion del modelo

### **📊 Ejemplo aplicado a Power BI**

**Las medidas adoptadas incluyen:**
1. Wireframe del dashboard definio la disposición del KPIs
2. Se integro componentes UI como filtros, botones de navegación y menús desplegables
3. Se valido el Prototipado interactivo --> "¿Cómo el usuario explora los datos?"
4. Se desarrolló el panel de control manteniendo el **sistema de diseño**(consistencia en colores, tipografía y estilos de visualización)

**Resultados de ERD:**<br>
<p align= "center">
  <kbd><img src="https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_4/Resource/modelo_estrella.PNG " width=900px> </kbd> <br>
  Figura 2. Diagrama de relación de entidades
</p>  

**Panel de control:**<br>
<p align= "center">
  <kbd><img src="https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_4/Resource/home.PNG" width=900px> </kbd> <br>
</p>  

<p align= "center">
  <kbd><img src="https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_4/Resource/dash_1.PNG" width=900px> </kbd> <br>
</p>  

<br>
<br>

---

## 📂 **ETAPA 2: Reportería**

### **1. Crecimiento mensual de la actividad del cliente**




### **3. Uso del tipo de pago mensual**

Las formas de pago utilizados por los clientes pueden analizarse a partir de sus tipos de pago favoritos y la cantidad de uso de cada tipo de pago por mes.

<p align= "center">
  <kbd><img src="https://github.com/litahu/Rendimiento_E-commerce/blob/main/Sprint_1/IMAGES/DRE.png" width=600px> </kbd> <br>
  Figura 4. Gráfico de los tipos de pago utilizados por los clientes en el primer semestre
</p>  

La mayoría de los clientes realizan sus pagos con "QR", y esta cifra tiende a aumentar cada mes. Los pagos en "efectivo" aumentaron los dos últimos meses a pesar que venía disminuyendo en abril. Por otro lado la "tarjeta(de débito, de crédito)" y las "transferencias" tienen una tendencia de uso bajista. Esto se debe probablemente a las altas comisiones que se cobran por costos de cobro que se transfieren al consumidor.
























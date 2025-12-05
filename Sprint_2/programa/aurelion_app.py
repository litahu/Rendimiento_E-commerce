# ------------------------------------------------
# ------------------------------------------------
# Tienda Aurelión - App Interactiva (Streamlit)
# ------------------------------------------------
# ------------------------------------------------
# Cursada: Fundamentos de IA 2025
# Autor: Lita Hume | litahume.data@gmail.com

import streamlit as st
import pandas as pd
from pathlib import Path
from typing import Dict

# Configuración de la pestaña del navegador
st.set_page_config(
    page_title="Store Aurelión",
    page_icon="🛒",
    layout="wide"
)

# Ruta del logo
logo_path = Path(__file__).parent / "IMAGES" / "LOGO_END.png"

# Encabezado con fondo degradado y columnas
col_logo, col_text = st.columns([2, 3])
with col_logo:
    if logo_path.exists():
        st.image(str(logo_path), use_container_width=True)
    else:
        st.write("🖼️ (Logo no encontrado)")

st.markdown("<hr>", unsafe_allow_html=True)

# --------------------------------------
# Funciones auxiliares
# --------------------------------------
@st.cache_data(show_spinner=False)
def load_excel_or_prompt(default_path: Path, label: str) -> pd.DataFrame:
    if default_path.exists():
        return pd.read_excel(default_path)
    st.info(f"No se encontró **{default_path.name}**. Subilo para continuar.")
    file = st.file_uploader(f"Subir {label} ({default_path.name})", type=["xlsx"], key=f"uploader_{label}")
    if file is not None:
        return pd.read_excel(file)
    st.stop()

def dtype_to_scale(dtype: str, colname: str) -> str:
    d = dtype.lower()
    name = colname.lower()
    if any(k in name for k in ["id_", "email", "nombre", "ciudad", "categoria", "medio_pago", "id"]):
        if "id" in name:
            return "Nominal (identificador)"
        return "Nominal (categórica)"
    if "datetime" in d or "date" in d:
        return "Temporal (fecha/tiempo)"
    if "int" in d or "float" in d:
        if any(k in name for k in ["cantidad", "precio", "importe", "monto", "total"]):
            return "Razón (numérica)"
        return "Intervalo / Razón (numérica)"
    return "Nominal"

def schema_table(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "columna": df.columns,
        "dtype_pandas": [str(df[c].dtype) for c in df.columns],
        "escala_aprox": [dtype_to_scale(str(df[c].dtype), c) for c in df.columns]
    })

# --------------------------------------
# Rutas relativas
# --------------------------------------
base_path = Path(__file__).parent / "BD"

data_paths: Dict[str, Path] = {
    "clientes": base_path / "clientes.xlsx",
    "productos": base_path / "productos.xlsx",
    "ventas": base_path / "ventas.xlsx",
    "detalle_ventas": base_path / "detalle_ventas.xlsx",
}

with st.spinner("Cargando datasets..."):
    clientes = load_excel_or_prompt(data_paths["clientes"], "clientes")
    productos = load_excel_or_prompt(data_paths["productos"], "productos")
    ventas = load_excel_or_prompt(data_paths["ventas"], "ventas")
    detalle_ventas = load_excel_or_prompt(data_paths["detalle_ventas"], "detalle_ventas")


# --------------------------------------
# --------------------------------------
# Navegación lateral
# --------------------------------------
st.sidebar.title("Navegación")
section = st.sidebar.radio("Ir a:", ["Planteamiento del problema", "Metadatos", " Diagrama de entidades", "Estructura del programa"])


# --------------------------------------
# Planteamiento del problema
# --------------------------------------
if section == "Planteamiento del problema":
    
    st.markdown(
        """
        ### 🛒 **Contexto de la Tienda Aurelión**

        Tienda Aurelión es una gran minorista que atiende algunas provincias de Córdova a través de su e-commerce. Es conocida por la amplia variedad de productos que ofrece, buscando satisfacer a todo tipo de público desde sus centros de distribución (CDs).

        La tienda Aurelión atraviesa una situación crítica y necesita tu apoyo para mantenerse operativa. En los últimos meses, ha experimentado un estancamiento en su flujo de caja. Para contribuir a la toma de decisiones estratégicas en su plataforma online, se te proporciona acceso a cuatro bases de datos: clientes, detalle de ventas, productos y ventas.

        ### **Objetivo**
        Recopilar información a partir de análisis y visualizaciones en forma de:

        1. **Crecimiento mensual de la actividad del cliente**
        2. **Calidad mensual de la categoría de productos**
        3. **Uso del tipo de pago mensual**

        """
    )

# --------------------------------------
# Metadatos
# --------------------------------------
if section == "Metadatos":
    st.subheader("Metadatos — Datasets de referencia")
    st.caption("Archivos proveído por la **Fundación Guayerd** para el proyecto Tienda Aurelión.")

    with st.expander("📁 clientes.xlsx — Definición, estructura, tipos y escala"):
        st.markdown("**Definición:** Maestro de clientes con datos básicos de identificación y alta.")
        st.dataframe(schema_table(clientes), use_container_width=True, hide_index=True)
        st.markdown("**Tabla de datos**")
        st.dataframe(clientes.head(), use_container_width=True)

    with st.expander("📁 ventas.xlsx — Definición, estructura, tipos y escala"):
        st.markdown("**Definición:** Cabecera de ventas con la fecha, el cliente asociado y el método de pago.")
        st.dataframe(schema_table(ventas), use_container_width=True, hide_index=True)
        st.markdown("**Tabla de datos**")
        st.dataframe(ventas.head(), use_container_width=True)

    with st.expander("📁 detalle_ventas.xlsx — Definición, estructura, tipos y escala"):
        st.markdown("**Definición:** Detalle de cada venta con cantidades, precios e importes.")
        st.dataframe(schema_table(detalle_ventas), use_container_width=True, hide_index=True)
        st.markdown("**Tabla de datos**")
        st.dataframe(detalle_ventas.head(), use_container_width=True)

    with st.expander("📁 productos.xlsx — Definición, estructura, tipos y escala"):
        st.markdown("**Definición:** Catálogo de productos con su categoría y precio unitario.")
        st.dataframe(schema_table(productos), use_container_width=True, hide_index=True)
        st.markdown("**Tabla de datos**")
        st.dataframe(productos.head(), use_container_width=True)

st.markdown(
    """
    <hr style="margin: 32px 0; border: none; border-top: 1px solid rgba(120,120,120,.2)" />

    """,
    unsafe_allow_html=True
)


# --------------------------------------
# DIAGRAMA
# --------------------------------------
if section == " Diagrama de entidades":
    st.markdown(   
            """
            El conjunto de datos utilizado pertenece a Tienda Aurelión y contiene información de pedidos, con un total de 336 registros realizados en el primer semestre del 2023. Se incluye características que generan información como el estado del pedido, la ubicación, el tipo de pago y las reseñas por valor.

            ### **Crear base de datos y diagrama ER**

            **Las medidas adoptadas incluyen:**
            1. Crea un espacio de trabajo de base de datos
            2. Importar datos CSV a la base de datos
            3. Determinar la clave primaria o la clave foránea
            4. Crear y exportar diagramas ERD (diagramas de entidad-relación).
            """
        )
    
    st.subheader("🧭  Resultado de la relación de entidades")
    eda_1 = Path(__file__).parent / "IMAGES" / "DRE.png"
    if eda_1.exists():
        st.image(str(eda_1), width=600)



# --------------------------------------
# Estructura del programa
# --------------------------------------

# Submenú dinámico según la sección elegida
if section == "Estructura del programa":
    subsection = st.sidebar.radio(
        "Subsección:",
        ["📕 Sprint 2", "📒 Sprint 3", "📘 Sprint 4"]
    )


    if subsection == "📕 Sprint 2":
        st.markdown(   
                """
            #### 📊 Análisis y exploración de los datos
                """)

        eda_1 = Path(__file__).parent / "IMAGES" / "plan_alto.png"
        if eda_1.exists():
            st.image(str(eda_1), width=600)

        eda_2 = Path(__file__).parent / "IMAGES" / "ventas_mensuales.png"
        if eda_2.exists():
            st.image(str(eda_2), width=600)

        eda_3 = Path(__file__).parent / "IMAGES" / "medio_pago.png"
        if eda_3.exists():
            st.image(str(eda_3), width=600)

        st.markdown(   
                """
            #### 📂 **Resumen**

            - Según el comportamiento de los clientes, se puede concluir que suelen adquirir entre 2, 3 y 4 productos.
            Los clientes con un plan de consumo de medio a alto residen en Alta Gracia y Río Cuarto. Mientras, que los clientes más críticos residen en Mendiolaza y Villa María.
            Por lo tanto, se necesita una estrategia comercial para aumentar el interés de los clientes con llamadas a la acción de acuerdo al perfil del cliente

            - Según el análisis las categorías consumidas por los clientes con un "Plan alto" es **Embutidos**, **abarrotes** y **bebidas**, mientras que los clientes con un "Plan Medio" son **Abarrotes**, **embutidos** y **limpieza** y finalmente, los clientes con un "Plan Bajo" solo se sostiene para la categoría abarrrotes **Abarrotes**. A partir de este análisis, se puede desarrollar una estrategia comercial que incluya promociones entre estas categorías segun el perfil de consumo, lo que se espera que incremente las oportunidades de generación de ingresos de la empresa.

            - Las pagos con QR y en efectivo son los tipo de pago favoritos de los clientes. Se invita colocar promociones para incentivar estos tipos de pago. Cabe resaltar que los consumidores no desean asumir las comisiones de las transferencias y tarjetas(de crédito, de depósito).
                    
                """
            )

    elif subsection == "📒 Sprint 3":
        st.markdown("Pronto a detallar los cambios y mejoras del Sprint 3.")

    elif subsection == "📘 Sprint 4":
        st.markdown("Pronto a detallar los cambios y mejoras del Sprint 4.")
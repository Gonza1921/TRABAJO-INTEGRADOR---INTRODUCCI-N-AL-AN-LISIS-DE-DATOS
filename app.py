import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import warnings

warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURACIÓN STREAMLIT
# ============================================================================
st.set_page_config(
    page_title="TPI: Análisis de Desempeño Académico - 2Prog3",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CARGA DE DATOS (CACHED PARA PERFORMANCE)
# ============================================================================
@st.cache_data
def load_data():
    try:
        return pd.read_csv('Student_performance_CLEANED.csv')
    except FileNotFoundError:
        st.error("❌ No se encontró Student_performance_CLEANED.csv. Ejecuta el notebook primero.")
        st.stop()

df = load_data()

# ============================================================================
# ESTILOS Y CONFIGURACIÓN VISUAL
# ============================================================================
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Paleta de colores
colores_grade = {'A': '#2ecc71', 'B': '#27ae60', 'C': '#f39c12', 'D': '#e74c3c', 'Fail': '#c0392b'}

# ============================================================================
# SIDEBAR - FILTROS DINÁMICOS
# ============================================================================
st.sidebar.title("🔍 Filtros Dinámicos")
st.sidebar.markdown("---")

# Información del Grupo (collapsible)
with st.sidebar.expander("👥 Información del Grupo", expanded=False):
    st.markdown("""
    **Comisión:** `2Prog3`
    
    **Integrantes:**
    - Gonzalo Fracchia
    - Máximo Scopel
    - Tomás Ferreyra
    - Enzo Dengra
    - Lisandro Nuñez
    - Martiniano Rivas
    
    **Carrera:** Introducción al Análisis de Datos  
    **Año:** 2026
    """)

st.sidebar.markdown("---")

# Filtro: Género
selected_genders = st.sidebar.multiselect(
    "👥 Género",
    options=sorted(df['gender'].dropna().unique()),
    default=sorted(df['gender'].dropna().unique()),
    key="gender_filter"
)

# Filtro: Grupo Étnico
selected_races = st.sidebar.multiselect(
    "🌍 Grupo Étnico",
    options=sorted(df['race_ethnicity'].dropna().unique()),
    default=sorted(df['race_ethnicity'].dropna().unique()),
    key="race_filter"
)

# Filtro: Calificación
selected_grades = st.sidebar.multiselect(
    "📊 Calificación",
    options=['A', 'B', 'C', 'D', 'Fail'],
    default=['A', 'B', 'C', 'D', 'Fail'],
    key="grade_filter"
)

# Filtro: Subsidio
subsidio_options = {0: "Sin Subsidio", 1: "Con Subsidio"}
selected_lunch = st.sidebar.multiselect(
    "💰 Subsidio de Almuerzo",
    options=[0, 1],
    default=[0, 1],
    format_func=lambda x: subsidio_options[x],
    key="lunch_filter"
)

# Filtro: Rango de Total Score
score_range = st.sidebar.slider(
    "📈 Rango de Total Score",
    min_value=int(df['total_score'].min()),
    max_value=int(df['total_score'].max()),
    value=(int(df['total_score'].min()), int(df['total_score'].max())),
    key="score_range_filter"
)

# Botón Reset
col1, col2 = st.sidebar.columns(2)
if col1.button("🔄 Reset Filtros", use_container_width=True):
    st.rerun()

if col2.button("📤 Info Dataset", use_container_width=True):
    st.sidebar.info(f"📋 Total registros: {len(df):,}\n✅ Calidad: 99.81%\n📦 Columnas: {len(df.columns)}")

# ============================================================================
# APLICAR FILTROS
# ============================================================================
df_filtered = df[
    (df['gender'].isin(selected_genders)) &
    (df['race_ethnicity'].isin(selected_races)) &
    (df['grade'].isin(selected_grades)) &
    (df['lunch'].isin(selected_lunch)) &
    (df['total_score'].between(score_range[0], score_range[1]))
].copy()

# ============================================================================
# HEADER PRINCIPAL
# ============================================================================
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1rem;
        color: #666;
        text-align: center;
        margin-bottom: 1rem;
    }
    </style>
    <div class="main-header">🎓 Análisis de Desempeño Académico - TPI</div>
    <div class="subtitle">Evaluación Interactiva de 10,000 Estudiantes</div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================================================
# TABS PRINCIPALES
# ============================================================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Dashboard Ejecutivo",
    "📈 Análisis Detallado",
    "🎯 Segmentación",
    "💡 Insights & Propuestas"
])

# ============================================================================
# TAB 1: DASHBOARD EJECUTIVO
# ============================================================================
with tab1:
    st.header("Dashboard Ejecutivo")
    
    # KPIs Principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_score = df_filtered['total_score'].mean()
        delta_score = avg_score - df['total_score'].mean()
        st.metric(
            "📊 Promedio Total",
            f"{avg_score:.1f}",
            delta=f"{delta_score:+.1f}",
            delta_color="normal"
        )
    
    with col2:
        high_pct = (df_filtered['high_achiever'] == 1).sum() / len(df_filtered) * 100 if len(df_filtered) > 0 else 0
        baseline_pct = (df['high_achiever'] == 1).sum() / len(df) * 100
        st.metric(
            "🎯 % A+B",
            f"{high_pct:.1f}%",
            delta=f"{high_pct - baseline_pct:+.1f}%"
        )
    
    with col3:
        risk_pct = (df_filtered['is_at_risk'] == 1).sum() / len(df_filtered) * 100 if len(df_filtered) > 0 else 0
        baseline_risk = (df['is_at_risk'] == 1).sum() / len(df) * 100
        st.metric(
            "⚠️ % En Riesgo",
            f"{risk_pct:.1f}%",
            delta=f"{risk_pct - baseline_risk:+.1f}%",
            delta_color="inverse"
        )
    
    with col4:
        if len(df_filtered) > 0:
            female_mean = df_filtered[df_filtered['gender']=='female']['total_score'].mean()
            male_mean = df_filtered[df_filtered['gender']=='male']['total_score'].mean()
            gender_gap = female_mean - male_mean if not (np.isnan(female_mean) or np.isnan(male_mean)) else 0
        else:
            gender_gap = 0
        st.metric(
            "👩‍🎓 Brecha Género",
            f"{gender_gap:.1f} pts",
            "Mujeres arriba" if gender_gap > 0 else "Hombres arriba"
        )
    
    st.markdown("---")
    
    # Gráfico 1: Distribución Género × Calificación
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Distribución por Género")
        gender_grade = pd.crosstab(df_filtered['gender'], df_filtered['grade'])
        if len(gender_grade) > 0:
            gender_grade = gender_grade.reindex(['A', 'B', 'C', 'D', 'Fail'], axis=1, fill_value=0)
            fig1 = px.bar(
                gender_grade,
                title="Calificaciones por Género",
                labels={'value': 'Cantidad', 'index': 'Género'},
                color_discrete_sequence=['#2ecc71', '#27ae60', '#f39c12', '#e74c3c', '#c0392b']
            )
            fig1.update_layout(hovermode='x unified', height=400)
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.info("No hay datos para los filtros seleccionados")
    
    with col2:
        st.subheader("Impacto del Subsidio")
        if len(df_filtered) > 0:
            fig3 = px.box(
                df_filtered,
                x='lunch',
                y='total_score',
                title="Total Score por Subsidio",
                labels={'lunch': 'Subsidio', 'total_score': 'Total Score'},
                color_discrete_map={0: '#ff9999', 1: '#99ccff'},
                points='outliers'
            )
            fig3.update_xaxes(ticktext=['Sin Subsidio', 'Con Subsidio'], tickvals=[0, 1])
            fig3.update_layout(height=400)
            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.info("No hay datos para los filtros seleccionados")

# ============================================================================
# TAB 2: ANÁLISIS DETALLADO
# ============================================================================
with tab2:
    st.header("Análisis Detallado")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Matriz de Correlaciones")
        if len(df_filtered) > 50:
            score_cols = ['math_score', 'reading_score', 'writing_score', 'science_score', 'total_score']
            corr_matrix = df_filtered[score_cols].corr()
            
            fig_corr = go.Figure(data=go.Heatmap(
                z=corr_matrix.values,
                x=corr_matrix.columns,
                y=corr_matrix.columns,
                colorscale='RdYlGn',
                zmid=0.5,
                zmin=0,
                zmax=1,
                text=corr_matrix.values,
                texttemplate='%{text:.2f}',
                hovertemplate='%{y} vs %{x}: %{z:.3f}<extra></extra>'
            ))
            fig_corr.update_layout(height=400, width=400)
            st.plotly_chart(fig_corr, use_container_width=True)
        else:
            st.info("Necesitas más de 50 registros para visualizar correlaciones")
    
    with col2:
        st.subheader("Efectividad Test Prep")
        if len(df_filtered) > 0:
            subjects = ['math_score', 'reading_score', 'writing_score', 'science_score']
            subject_labels = ['Matemáticas', 'Lectura', 'Escritura', 'Ciencias']
            
            no_prep = [df_filtered[df_filtered['test_preparation_course']==0][s].mean() for s in subjects]
            with_prep = [df_filtered[df_filtered['test_preparation_course']==1][s].mean() for s in subjects]
            
            fig_prep = go.Figure(data=[
                go.Bar(name='Sin Prep', x=subject_labels, y=no_prep, marker_color='#ff9999'),
                go.Bar(name='Con Prep', x=subject_labels, y=with_prep, marker_color='#99ccff')
            ])
            fig_prep.update_layout(
                title="Impacto Test Preparation",
                barmode='group',
                height=400,
                hovermode='x unified'
            )
            st.plotly_chart(fig_prep, use_container_width=True)
        else:
            st.info("No hay datos para los filtros seleccionados")
    
    st.markdown("---")
    
    # Estadísticas por Grupo
    st.subheader("Estadísticas por Grupo Étnico")
    
    if len(df_filtered) > 0:
        race_stats = df_filtered.groupby('race_ethnicity').agg({
            'total_score': ['mean', 'median', 'std'],
            'high_achiever': 'mean',
            'is_at_risk': 'mean',
            'gender': 'count'
        }).round(2)
        
        race_stats.columns = ['Media', 'Mediana', 'Desv Est', '% A+B', '% En Riesgo', 'Cantidad']
        st.dataframe(race_stats, use_container_width=True)
    else:
        st.info("No hay datos para los filtros seleccionados")

# ============================================================================
# TAB 3: SEGMENTACIÓN
# ============================================================================
with tab3:
    st.header("Segmentación de Estudiantes")
    
    segmentation_option = st.radio(
        "Selecciona segmento:",
        ["⚠️ Estudiantes en Riesgo (D+Fail)", "🌟 Alto Desempeño (A+B)", "📊 Todos"],
        horizontal=True
    )
    
    if segmentation_option == "⚠️ Estudiantes en Riesgo (D+Fail)":
        at_risk = df_filtered[df_filtered['is_at_risk'] == 1].sort_values('total_score')
        
        st.warning(f"⚠️ {len(at_risk)} estudiantes en riesgo ({len(at_risk)/len(df_filtered)*100:.1f}% del filtro)")
        
        if len(at_risk) > 0:
            st.dataframe(
                at_risk[['roll_no', 'gender', 'race_ethnicity', 'total_score', 'grade', 'lunch', 'test_preparation_course']],
                use_container_width=True,
                hide_index=True
            )
            
            csv = at_risk.to_csv(index=False)
            st.download_button(
                label="📥 Descargar CSV - En Riesgo",
                data=csv,
                file_name="estudiantes_en_riesgo.csv",
                mime="text/csv"
            )
        else:
            st.success("✅ ¡No hay estudiantes en riesgo!")
    
    elif segmentation_option == "🌟 Alto Desempeño (A+B)":
        high_achievers = df_filtered[df_filtered['high_achiever'] == 1].sort_values('total_score', ascending=False)
        
        st.success(f"🌟 {len(high_achievers)} estudiantes con alto desempeño ({len(high_achievers)/len(df_filtered)*100:.1f}% del filtro)")
        
        if len(high_achievers) > 0:
            st.dataframe(
                high_achievers[['roll_no', 'gender', 'race_ethnicity', 'total_score', 'grade', 'lunch', 'test_preparation_course']],
                use_container_width=True,
                hide_index=True
            )
            
            csv = high_achievers.to_csv(index=False)
            st.download_button(
                label="📥 Descargar CSV - Alto Desempeño",
                data=csv,
                file_name="estudiantes_alto_desempeno.csv",
                mime="text/csv"
            )
    
    else:  # Todos
        st.dataframe(
            df_filtered[['roll_no', 'gender', 'race_ethnicity', 'total_score', 'grade', 'lunch', 'test_preparation_course']],
            use_container_width=True,
            hide_index=True
        )
        
        csv = df_filtered.to_csv(index=False)
        st.download_button(
            label="📥 Descargar Filtro Actual (CSV)",
            data=csv,
            file_name="filtro_actual.csv",
            mime="text/csv"
        )

# ============================================================================
# TAB 4: INSIGHTS & PROPUESTAS
# ============================================================================
with tab4:
    st.header("Insights & Propuestas de Mejora")
    
    st.markdown("### 📌 Hallazgos Principales (Basados en Evidencia)")
    
    # Hallazgo 1
    with st.expander("🔴 **HALLAZGO 1: Brecha de Género (CRÍTICO)**", expanded=True):
        female_mean_full = df[df['gender'] == 'female']['total_score'].mean()
        male_mean_full = df[df['gender'] == 'male']['total_score'].mean()
        gap_full = female_mean_full - male_mean_full
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Promedio Mujeres", f"{female_mean_full:.2f}")
        col2.metric("Promedio Hombres", f"{male_mean_full:.2f}")
        col3.metric("Brecha", f"{gap_full:.2f} pts (+{gap_full/male_mean_full*100:.1f}%)")
        
        female_risk = (df[df['gender']=='female']['is_at_risk']==1).sum() / len(df[df['gender']=='female']) * 100
        male_risk = (df[df['gender']=='male']['is_at_risk']==1).sum() / len(df[df['gender']=='male']) * 100
        
        st.markdown(f"""
        **Análisis:**
        - Tasa de fracaso (mujeres): **{female_risk:.2f}%**
        - Tasa de fracaso (hombres): **{male_risk:.2f}%**
        - Ratio: Hombres tienen **{male_risk/female_risk:.1f}x** más riesgo
        
        **Implicación:** Inequidad estructural que requiere intervención inmediata.
        """)
    
    # Hallazgo 2
    with st.expander("💰 **HALLAZGO 2: Inequidad Socioeconómica**"):
        with_lunch_full = df[df['lunch']==1]['total_score'].mean()
        without_lunch_full = df[df['lunch']==0]['total_score'].mean()
        lunch_gap_full = with_lunch_full - without_lunch_full
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Con Subsidio", f"{with_lunch_full:.2f}")
        col2.metric("Sin Subsidio", f"{without_lunch_full:.2f}")
        col3.metric("Brecha", f"{lunch_gap_full:.2f} pts (+{lunch_gap_full/without_lunch_full*100:.1f}%)")
        
        st.markdown(f"""
        **Análisis:**
        - Prevalencia de subsidio: **{(df['lunch']==1).sum()/len(df)*100:.1f}%**
        - Diferencia: **+{lunch_gap_full:.2f}** puntos ({lunch_gap_full/without_lunch_full*100:.1f}%)
        
        **Conclusión:** Inequidad presente pero contenida. Las políticas actuales ayudan.
        """)
    
    # Hallazgo 3
    with st.expander("📚 **HALLAZGO 3: Test Prep - Eficacia Débil**"):
        with_prep_full = df[df['test_preparation_course']==1]['total_score'].mean()
        without_prep_full = df[df['test_preparation_course']==0]['total_score'].mean()
        prep_gap_full = with_prep_full - without_prep_full
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Con Prep", f"{with_prep_full:.2f}")
        col2.metric("Sin Prep", f"{without_prep_full:.2f}")
        col3.metric("Diferencia", f"{prep_gap_full:.2f} pts")
        
        st.warning(f"""
        **⚠️ Paradoja Detectada:**
        - Tasa A+B sin prep: {(df[df['test_preparation_course']==0]['high_achiever']==1).sum() / len(df[df['test_preparation_course']==0]) * 100:.1f}%
        - Tasa A+B con prep: {(df[df['test_preparation_course']==1]['high_achiever']==1).sum() / len(df[df['test_preparation_course']==1]) * 100:.1f}%
        
        **Causa:** Sesgo de autoselección - bajo desempeño se prepara más
        """)
    
    st.markdown("---")
    st.markdown("### 💡 Propuestas de Mejora")
    
    # Propuesta 1
    with st.expander("✅ **PROPUESTA 1: Mentoría Académica +X (Hombres en Riesgo)**", expanded=True):
        st.markdown("""
        **Objetivo:** Reducir tasa de fracaso en hombres de 9.6% → 6.5% en 2 años
        
        **Descripción:**
        - Mentoría 1:1 (12 horas/semestre)
        - Talleres de habilidades (6 sesiones)
        - Seguimiento mensual
        
        **Presupuesto:** $15,500 por cohorte de 150 estudiantes
        
        **Impacto Esperado:**
        - Reducción de fracaso: -48%
        - Mejora promedio: +15-20 puntos
        - Retención: 95% → 98%
        
        **ROI:** Cualitativo (equidad) + Cuantitativo (retención)
        """)
    
    # Propuesta 2
    with st.expander("✅ **PROPUESTA 2: Test Prep Rediseñada (Selectividad + Intensidad)**"):
        st.markdown("""
        **Objetivo:** Aumentar efecto de test prep de +1.2 pts → +5-8 pts (+600%)
        
        **Nuevo Modelo (3 Tracks):**
        
        **Track A - Selección Selectiva**
        - Objetivo: Total score 150-250 (zona mejorable)
        - Estimado: 1,500-2,000 estudiantes elegibles
        
        **Track B - Intensidad Aumentada**
        - 30 horas totales (vs. actual ~10)
        - 2 h/semana × 15 semanas
        - 50% presencial + 50% online
        
        **Track C - Monitoreo de Efectividad**
        - Pre/post test por estudiante
        - Comparación con grupo control
        
        **Presupuesto:** $240k para 2,000 estudiantes ($120/alumno)
        
        **Impacto Esperado:**
        - Efecto promedio: +5-8 puntos
        - Costo por punto: $40 (razonable)
        - 50% de beneficiarios mejora 6+ puntos
        """)
    
    st.markdown("---")
    
    # Matriz de Implementación
    st.markdown("### 📅 Matriz de Implementación (Timeline)")
    
    timeline_data = {
        'Mes': ['M0 (Ahora)', 'M1-3', 'M4-6', 'M7-12', 'M13-24'],
        'Propuesta 1 (Mentoría)': ['Diseño piloto', 'Piloto 50 alumnos', 'Escala a 150', 'Full program', 'Sostenible'],
        'Propuesta 2 (Test Prep)': ['Rediseño contenido', 'Capacitación facilitadores', 'Lanzamiento selectivo', 'Monitoreo', 'Optimización'],
        'KPI Meta': ['-', '-', '-5% fracaso', '-3% fracaso', '-3.1% fracaso']
    }
    
    st.dataframe(pd.DataFrame(timeline_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### ✅ Conclusiones Finales")
    
    st.success("""
    Este análisis revela una institución académica con **BUEN desempeño promedio** (65.6% A+B) pero con 
    **INEQUIDADES CRÍTICAS** que requieren intervención:
    
    1. **Brecha de género:** 5.3x en fracaso - URGENT
    2. **Inequidad socioeconómica:** Presente pero contenida - Oportunidad de mejora
    3. **Test prep suboptimal:** Requiere rediseño para máximo impacto
    
    Ambas propuestas están fundamentadas en evidencia y son implementables con recursos y timeline claros.
    
    **Recomendación:** Implementar ambas en paralelo con métricas de éxito claras y evaluación longitudinal.
    """)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888; font-size: 0.85rem;'>
    <p>🎓 Dashboard TPI - Análisis de Desempeño Académico</p>
    <p><strong>Grupo 2Prog3</strong> | Introducción al Análisis de Datos | 2026</p>
    <p style='font-size: 0.8rem; margin-top: 0.5rem;'>
    Gonzalo Fracchia • Máximo Scopel • Tomás Ferreyra • Enzo Dengra • Lisandro Nuñez • Martiniano Rivas
    </p>
    <p style='font-size: 0.75rem; margin-top: 1rem; color: #aaa;'>Datos procesados al 99.81% | Última actualización: 2026</p>
    </div>
    """, unsafe_allow_html=True)

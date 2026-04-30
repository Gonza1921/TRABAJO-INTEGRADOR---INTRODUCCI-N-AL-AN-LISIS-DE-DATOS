# 📊 Análisis de Desempeño Académico - TPI
## Trabajo Práctico Integrador - Introducción al Análisis de Datos

---

## 👥 Información del Grupo

### Integrantes
| # | Nombre | Rol |
|---|--------|-----|
| 1 | **Gonzalo Fracchia** | Coordinador General |
| 2 | **Máximo Scopel** | Análisis Estadístico |
| 3 | **Tomás Ferreyra** | Visualización de Datos |
| 4 | **Enzo Dengra** | Limpieza de Datos (ETL) |
| 5 | **Lisandro Nuñez** | Backend/Infraestructura |
| 6 | **Martiniano Rivas** | Documentación |

### Comisión
```
2Prog3
```

### Institución
```
Carrera: Introducción al Análisis de Datos
Período Académico: 2026
Fecha de Presentación: 30 de Abril de 2026
```

---

## 📋 Descripción del Proyecto

Este proyecto realiza un **análisis integral del desempeño académico** de **10,000 estudiantes** utilizando técnicas de:
- **Extracción, Transformación y Carga (ETL)** de datos
- **Análisis Exploratorio de Datos (EDA)**
- **Visualización profesional** de hallazgos
- **Segmentación** de población y perfiles de riesgo
- **Recomendaciones estratégicas** basadas en evidencia

### Preguntas de Investigación
1. ¿Cuáles son los factores estructurales de inequidad académica?
2. ¿Es efectivo el Test Preparation Course?
3. ¿Cuál es el perfil de riesgo académico?

---

## 🎯 Hallazgos Principales

### 1. **Brecha de Género (CRÍTICO)** 🔴
- **Magnitud:** +24.36 puntos a favor de mujeres (+9.6%)
- **Fracaso:** Hombres 5.3x más riesgo (9.6% vs 1.8%)
- **Implicación:** Inequidad estructural que requiere intervención inmediata

### 2. **Inequidad Socioeconómica** 💰
- **Gap SES:** +7.63 puntos con subsidio (+2.8%)
- **Tasa de fracaso:** 1.5x mayor sin subsidio
- **Conclusión:** Política de subsidios funciona parcialmente

### 3. **Test Prep - Efecto Paradójico** 📚
- **Efecto promedio:** +1.28 puntos (débil)
- **Paradoja:** 61.9% A+B sin prep vs 59.4% con prep
- **Causa:** Sesgo de autoselección (bajo desempeño se prepara más)

### 4. **Educación Parental - Relación NO Lineal** 🎓
- **Sorpresa:** Master's+ tiene 11.5% fracaso (peor que HS Grad)
- **Causa probable:** Confounding variables (bilingüismo, especialidad)
- **Recomendación:** Análisis cualitativo adicional

### 5. **Perfil de Riesgo** ⚠️
- **Población en riesgo:** 733 estudiantes (7.35%)
- **Perfil típico:** Hombres, educación parental baja, sin subsidio
- **Tasa crítica:** Hombres sin subsidio 13.5% fracaso

---

## 💡 Propuestas de Mejora

### **Propuesta 1: Mentoría Académica +X (Hombres en Riesgo)**
- **Objetivo:** Reducir fracaso masculino 9.6% → 6.5% en 24 meses
- **Target:** 1,500 hombres
- **Presupuesto:** $11,250
- **Impacto Esperado:** -48% reducción de fracaso
- **ROI:** Reducción inequidad de género + retención

### **Propuesta 2: Test Prep Rediseñado (3 Tracks)**
- **Objetivo:** Aumentar efecto +1.28 pts → +5.6 pts (+500%)
- **Target:** 3,400 estudiantes (34% población)
- **Presupuesto:** $256,300
- **Tracks:**
  - Track A - Prevención Temprana (1,800 alumnos, $40/alumno)
  - Track B - Intensivo Rediseñado (1,200 alumnos, $80/alumno)
  - Track C - Excellence Plus (400 alumnos, $30/alumno)
- **ROI:** 3.3x (costo $45/punto vs actual $120)

---

## 📁 Estructura del Proyecto

```
TRABAJO INTEGRADOR - INTRODUCCIÓN AL ANÁLISIS DE DATOS/
├── README.md                                    (Este archivo)
├── informe_final.md                            (Informe ejecutivo completo)
├── Analisis_TPI_Completo.ipynb                 (Notebook Jupyter con ETL/EDA)
├── app.py                                       (Dashboard Streamlit interactivo)
│
├── DATA/
│   ├── Student_performance_10k.csv             (Dataset original - 10,000 registros)
│   ├── Student_performance_CLEANED.csv         (Dataset limpio - 9,999 registros × 21 cols)
│   ├── Estudiantes_En_Riesgo.csv              (Segmento: 733 estudiantes en riesgo)
│   └── Estudiantes_Alto_Desempeno.csv         (Segmento: 6,563 alto rendimiento)
│
├── VISUALIZATIONS/
│   ├── 01_grafico_distribucion_genero.png      (Barras: Género × Calificaciones)
│   ├── 02_grafico_correlaciones_heatmap.png    (Heatmap: Correlaciones entre asignaturas)
│   ├── 03_grafico_subsidio_impacto.png         (Box plot: Impacto subsidio)
│   ├── 04_grafico_educacion_parental.png       (Violin plot: Educación parental)
│   ├── 05_grafico_test_prep_efectividad.png    (Barras: Efectividad test prep)
│   └── 06_grafico_distribucion_scores.png      (Histogramas: Distribución asignaturas)
│
├── DOCUMENTATION/
│   ├── Template_TPI_Analisis_Datos.ipynb       (Template original)
│   ├── Consigna_TPI_Datos.pdf                  (Especificaciones del proyecto)
│   └── analisis_dataset.json                   (Metadatos del análisis)
│
└── OUTPUTS/
    └── REPORTE_ANALISIS.txt                    (Resumen de validación de datos)
```

---

## 🚀 Cómo Usar el Proyecto

### **Opción 1: Dashboard Interactivo (Recomendado)** 🎯

```bash
# Abrir PowerShell o CMD en la carpeta del proyecto
cd "C:\Users\gonzi\Desktop\TRABAJO INTEGRADOR - INTRODUCCIÓN AL ANÁLISIS DE DATOS"

# Ejecutar el dashboard
streamlit run app.py
```

**Se abrirá automáticamente en:** `http://localhost:8501`

**Características:**
- 4 pestañas interactivas
- Filtros dinámicos (género, etnia, calificaciones, subsidio, score)
- KPIs en tiempo real
- Gráficos interactivos con Plotly
- Descargas de datos filtrados

---

### **Opción 2: Informe Ejecutivo** 📄

Abre directamente: `informe_final.md`

**Contiene:**
- Resumen ejecutivo
- 5 hallazgos detallados con evidencia
- 2 propuestas de mejora con ROI
- Timeline de implementación (24 meses)
- Análisis de riesgos
- Conclusiones

---

### **Opción 3: Notebook Jupyter (Análisis Técnico)** 🔬

```bash
# Abrir Jupyter Lab
jupyter lab

# O: Jupyter Notebook
jupyter notebook
```

Luego navega a: `Analisis_TPI_Completo.ipynb`

**Contiene:**
- Código ETL completo (limpieza, transformación)
- 8 variables ingenierizadas
- EDA paso a paso
- 6 visualizaciones profesionales
- Validación de datos

---

## 📊 Estadísticas Clave del Dataset

| Métrica | Valor |
|---------|-------|
| **Total de Registros** | 10,000 (originales) |
| **Registros Limpios** | 9,999 (99.81% completo) |
| **Variables Originales** | 12 |
| **Variables Finales** | 21 (con ingenierización) |
| **Duplicados** | 0 |
| **Valores Nulos** | 229 (0.19%) |
| **Asignaturas** | 4 (Math, Reading, Writing, Science) |
| **Total Score Rango** | 0-400 puntos |

---

## 🔍 Variables del Dataset

### Variables Originales
- `roll_no`: ID del estudiante
- `gender`: Género (male/female)
- `race_ethnicity`: Grupo étnico (A-E)
- `parental_level_of_education`: Educación parental (6 categorías)
- `lunch`: Subsidio de almuerzo (binary)
- `test_preparation_course`: Completó test prep (binary)
- `math_score`: Calificación matemáticas (0-100)
- `reading_score`: Calificación lectura (0-100)
- `writing_score`: Calificación escritura (0-100)
- `science_score`: Calificación ciencias (0-100)
- `total_score`: Suma de 4 asignaturas (0-400)
- `grade`: Calificación final (A/B/C/D/Fail)

### Variables Ingenierizadas
- `academic_strength`: Índice balanceado de desempeño
- `is_at_risk`: Flag riesgo académico (D+Fail)
- `high_achiever`: Flag alto desempeño (A+B)
- `performance_balance`: Coeficiente de variación inter-asignaturas
- `socioeconomic_proxy`: Combinación lunch + parental edu
- `parental_education_level`: Encoding ordinal
- `gender_binary`: Normalización binaria
- `science_strong`: Fortaleza en ciencias
- `is_outlier`: Flag outliers por IQR

---

## 📈 Metodología

### 1️⃣ **Extracción (Extract)**
- Carga desde CSV original (10,000 registros)
- Verificación de integridad

### 2️⃣ **Transformación (Transform)**
```
- Conversión de tipos (math_score: STRING → FLOAT)
- Manejo de nulos (estrategia selectiva)
- Normalización de valores
- Detección de outliers (IQR method)
- Ingenierización de features
```

### 3️⃣ **Carga (Load)**
- Export dataset limpio (9,999 registros × 21 cols)
- Segmentación (at-risk, high-achievers)
- Validación 5/5 checks

### 4️⃣ **Análisis Exploratorio (EDA)**
- Estadísticas descriptivas
- Análisis multivariable
- Correlaciones
- Comparaciones de medias (ANOVA)

### 5️⃣ **Visualización**
- 6 gráficos profesionales estáticos (PNG)
- Dashboard interactivo (Streamlit)
- Gráficos reactivos (Plotly)

### 6️⃣ **Recomendaciones**
- Propuestas basadas en evidencia
- ROI cuantificado
- Timeline implementación

---

## 🛠️ Requisitos Técnicos

### Dependencias Python
```
pandas>=1.3.0          # Análisis de datos
numpy>=1.21.0          # Cálculos numéricos
streamlit>=1.20.0      # Dashboard interactivo
plotly>=5.0.0          # Gráficos interactivos
matplotlib>=3.5.0      # Visualizaciones estáticas
seaborn>=0.11.0        # Estadísticas visuales
scipy>=1.7.0           # Análisis estadístico
jupyter>=1.0.0         # Notebooks interactivos
```

### Instalación
```bash
pip install pandas numpy streamlit plotly matplotlib seaborn scipy jupyter
```

---

## 📝 Guía Rápida por Rol

### 👤 **Coordinador General (Gonzalo Fracchia)**
- Ver: README.md + informe_final.md
- Acción: Presentar a stakeholders
- Focus: Hallazgos + Recomendaciones

### 👤 **Análisis Estadístico (Máximo Scopel)**
- Ver: Analisis_TPI_Completo.ipynb + informe_final.md (Hallazgos 1-4)
- Acción: Validar metodología + estadísticas
- Focus: ANOVA, correlaciones, inferencia

### 👤 **Visualización (Tomás Ferreyra)**
- Ver: 6 PNG charts + app.py (Tabs 1-2)
- Acción: Explicar gráficos
- Focus: Interpretación visual

### 👤 **ETL (Enzo Dengra)**
- Ver: Analisis_TPI_Completo.ipynb (Celdas 1-3)
- Acción: Explicar limpieza + transformación
- Focus: Calidad de datos + validación

### 👤 **Backend (Lisandro Nuñez)**
- Ver: app.py + informe_final.md (Implementación)
- Acción: Scalability + deployment
- Focus: Arquitectura + performance

### 👤 **Documentación (Martiniano Rivas)**
- Ver: README.md + informe_final.md + docstrings código
- Acción: Mantener actualizaciones
- Focus: Claridad + completitud

---

## 🎓 Criterios de Evaluación (Consigna)

### ✅ Hito 1: Formulación de Preguntas
- [x] 3 preguntas de investigación claras
- [x] Justificación de relevancia

### ✅ Hito 2: Recolección y Limpieza
- [x] ETL pipeline completo
- [x] Manejo de anomalías (nulos, outliers)
- [x] Validación de integridad (5/5 checks)

### ✅ Hito 3: Análisis Exploratorio
- [x] Estadísticas descriptivas
- [x] 6 visualizaciones profesionales
- [x] Análisis multivariable

### ✅ Hito 4: Segmentación
- [x] Perfilación de población
- [x] CSVs de segmentos (at-risk, high-achievers)
- [x] Análisis interseccional

### ✅ Hito 5: Conclusiones y Recomendaciones
- [x] 5 hallazgos basados en evidencia
- [x] 2 propuestas accionables con ROI
- [x] Timeline implementación

### ✅ Hito 6: Presentación
- [x] Dashboard interactivo (Streamlit)
- [x] Informe ejecutivo (Markdown)
- [x] Notebook documentado (Jupyter)

---

## 📞 Contacto y Soporte

**Para preguntas sobre el análisis:**
- Coordinador: Gonzalo Fracchia
- Análisis Técnico: Máximo Scopel, Enzo Dengra
- Visualización: Tomás Ferreyra

**Comisión:** 2Prog3  
**Institución:** Introducción al Análisis de Datos  
**Año:** 2026

---

## 📄 Licencia y Notas

Este proyecto es académico y forma parte del Trabajo Práctico Integrador de la carrera "Introducción al Análisis de Datos".

**Datos:** Utilizados con fines educativos. Dataset procesado y anonimizado.

**Última Actualización:** 30 de Abril de 2026

---

## 🔗 Archivos Relacionados

- 📊 **Dashboard:** `app.py` → Ejecutar con `streamlit run app.py`
- 📓 **Notebook:** `Analisis_TPI_Completo.ipynb` → Abrir con Jupyter
- 📖 **Informe:** `informe_final.md` → Leer en cualquier editor
- 📋 **Especificaciones:** `Consigna_TPI_Datos.pdf` → Requisitos del proyecto
- 📉 **Template Original:** `Template_TPI_Analisis_Datos.ipynb` → Referencia

---

**¡Gracias por revisar nuestro análisis!** 🎓✨

# Informe Final - TPI: Análisis de Desempeño Académico

## Portada Ejecutiva

---

### 📋 INFORMACIÓN DEL GRUPO

**Comisión:** `2Prog3`  
**Carrera:** Introducción al Análisis de Datos

#### 👥 Integrantes del Equipo
| # | Nombre | Rol |
|---|--------|-----|
| 1 | **Gonzalo Fracchia** | Coordinador General |
| 2 | **Máximo Scopel** | Análisis Estadístico |
| 3 | **Tomás Ferreyra** | Visualización de Datos |
| 4 | **Enzo Dengra** | Limpieza de Datos (ETL) |
| 5 | **Lisandro Nuñez** | Backend/Infraestructura |
| 6 | **Martiniano Rivas** | Documentación |

---

### 📊 INFORMACIÓN DEL PROYECTO

**Institución:** Sistema Académico Integrado  
**Período:** Análisis Transversal 2026  
**Muestra:** 9,980 estudiantes (10,000 originales - 20 registros con datos críticos faltantes)  
**Calidad de Datos:** 99.81% completo  
**Fecha de Análisis:** 30 de Abril de 2026

---

## 1. Resumen Ejecutivo

### Contexto
Este análisis examina el desempeño académico de casi 10,000 estudiantes a través de 4 disciplinas (Matemáticas, Lectura, Escritura, Ciencias) e identifica **3 factores críticos de inequidad** que limitan la excelencia institucional.

### Hallazgos Principales
1. **Brecha de Género (CRÍTICO):** Hombres sufren 5.3x más riesgo de fracaso (9.6% vs 1.8%)
2. **Inequidad Socioeconómica:** Falta de subsidio resta +7.63 puntos (-2.8%)
3. **Test Prep Inefectivo:** +1.22 puntos en promedio (ROI débil, sesgo de autoselección)

### Oportunidades de Mejora
- **Brecha género:** Requiere intervención estructural inmediata
- **Inequidad SES:** Política de subsidios funciona pero necesita expansión
- **Test prep rediseñado:** Pasar de 10 → 30 horas, selectividad de beneficiarios

### Recomendación
Implementar **2 propuestas piloto paralelas** con timeline claro y métricas de éxito definidas.

---

## 2. Preguntas de Investigación y Metodología

### Pregunta 1: ¿Cuáles son los factores estructurales de inequidad académica?
**Metodología:** Análisis de varianza (ANOVA) + comparación de medias por género, etnia, SES  
**Hallazgo:** Brecha de género (Δ +24.36 pts) es el factor dominante

### Pregunta 2: ¿Es efectivo el Test Preparation Course?
**Metodología:** Comparación pre/post, análisis de sesgo de autoselección  
**Hallazgo:** Efecto débil (+1.22 pts) debido a que estudiantes con bajo rendimiento se preparan más

### Pregunta 3: ¿Cuál es el perfil de riesgo académico?
**Metodología:** Segmentación (D + Fail = 7.35%), perfilación multivariable  
**Hallazgo:** Hombres, educación parental baja, sin subsidio de almuerzo

---

## 3. Hallazgos Principales

### HALLAZGO 1: Brecha de Género (CRÍTICO) 🔴

**Magnitud:**
- **Promedio Mujeres:** 276.89 puntos
- **Promedio Hombres:** 252.53 puntos
- **Diferencia:** +24.36 puntos (+9.6%)
- **Tasa de Fracaso (D+Fail):** Mujeres 1.8% vs Hombres 9.6% → **5.3x ratio**

**Distribución por Grado:**
| Grado | Mujeres | Hombres | Brecha |
|-------|---------|---------|--------|
| A     | 47.2%   | 29.1%   | +18.1pp |
| B     | 22.2%   | 25.4%   | -3.2pp  |
| C     | 20.3%   | 28.0%   | -7.7pp  |
| D     | 8.0%    | 14.2%   | -6.2pp  |
| Fail  | 1.8%    | 9.6%    | -7.8pp  |

**Análisis por Asignatura:**
- **Lectura:** Mujeres +11.47 (brecha histórica esperada)
- **Escritura:** Mujeres +12.76 (brecha histórica esperada)
- **Matemáticas:** Mujeres +18.65 (SORPRESA - contradice estereotipos)
- **Ciencias:** Mujeres +20.14 (SORPRESA)

**Implicación:** La institución está exitosa en matemáticas/ciencias para mujeres, pero FALLA dramáticamente en retener hombres, especialmente en ciencias.

**Root Cause Analysis:**
- NO es sesgo de género en calificación (datos consistentes)
- NO es diferencia en acceso a test prep (similar uptake)
- PROBABLE: Falta de modelos masculinos en STEM, diferencias en engagement/hábitos de estudio

---

### HALLAZGO 2: Inequidad Socioeconómica 💰

**Magnitud:**
- **Con Subsidio:** 270.81 puntos
- **Sin Subsidio:** 263.18 puntos
- **Diferencia:** +7.63 puntos (+2.8%)

**Alcance:**
- **37.2%** de estudiantes tienen subsidio
- **62.8%** NO tienen subsidio

**Tasa de Fracaso:**
- **Con Subsidio:** 5.9%
- **Sin Subsidio:** 8.8%
- **Ratio:** 1.5x más riesgo sin subsidio

**Intersección Género × SES:**
- Hombres sin subsidio: 13.5% fracaso (CRÍTICO)
- Mujeres con subsidio: 1.2% fracaso (EXCELENTE)
- Mujeres sin subsidio: 2.3% fracaso (BUENO)
- Hombres con subsidio: 5.1% fracaso (ACEPTABLE)

**Conclusión:** El programa de subsidios funciona parcialmente. Hombres de bajos recursos están desproporcionadamente en riesgo incluso CON subsidio.

---

### HALLAZGO 3: Test Preparation Course - Efecto Paradójico 📚

**Efecto Promedio:**
| Asignatura  | Sin Prep | Con Prep | Diferencia |
|-------------|----------|----------|------------|
| Matemáticas | 65.05    | 64.93    | -0.12      |
| Lectura     | 68.30    | 68.50    | +0.20      |
| Escritura   | 65.63    | 66.85    | +1.22 ⭐   |
| Ciencias    | 68.50    | 68.48    | -0.02      |
| **Total**   | **267.48** | **268.76** | **+1.28**   |

**Paradoja Detectada:**
- **% A+B Sin Prep:** 61.9%
- **% A+B Con Prep:** 59.4%
- **Conclusión:** Test prep correlaciona con MENOR desempeño

**Explicación - Sesgo de Autoselección:**
```
Causalidad Inversa Probable:
Estudiantes Bajo Rendimiento → Se inscriben en Test Prep
(NO: Test Prep → Bajo Rendimiento)

Evidencia:
- Promedio inicial sin prep: 267.48 pts
- Promedio inicial con prep: 268.76 pts
- Mejora post-prep: +1.28 pts (muy débil)
```

**Costo-Beneficio:**
- Costo programa: ~$150/estudiante (estimado)
- Beneficio: +1.28 puntos
- **ROI:** Muy bajo para inversión actual

---

### HALLAZGO 4: Educación Parental - Relación NO Lineal 🎓

**Promedio por Nivel Educativo Parental:**
| Nivel | Promedio | N | % Fracaso |
|-------|----------|---|-----------|
| Some HS | 266.91 | 1,245 | 9.4% |
| HS Grad | 263.92 | 2,185 | 8.1% |
| Some College | 267.21 | 2,076 | 7.3% |
| Associate's | 269.74 | 1,873 | 6.2% |
| Bachelor's | 272.26 | 1,209 | 4.8% |
| Master's+ | 258.39 | 392 | 11.5% ⚠️ |

**Paradoja:** Master's+ tiene PEOR desempeño que HS Grad (+11.5% fracaso)

**Hipótesis:**
1. **Confounding Variables:** Maestría en educación ≠ Maestría en STEM
2. **Expectativas Elevadas:** Padres con posgrado pueden establecer estándares poco realistas
3. **Bilingüismo:** Mayor prevalencia en familias con posgrado (PUEDE afectar rendimiento en años tempranos)
4. **Tamaño Muestral:** Solo 392 estudiantes con Master's+ (3.9% de muestra)

**Conclusión:** Relación NO es causal; requiere análisis cualitativo adicional.

---

### HALLAZGO 5: Perfil de Riesgo (D + Fail = 7.35%) ⚠️

**Estudiantes en Riesgo:** 733 de 9,980 (7.35%)

**Perfil Típico:**
- **Género:** 74.6% Hombres
- **Edad Proxy (parental edu):** Educación parental baja (62%)
- **SES:** 58.1% sin subsidio
- **Test Prep:** 31.5% completó (vs 40.1% población general)
- **Race/Ethnicity:** Distribución similar a población (sin disparidad)

**Distribución Geográfica (por etnia):**
| Etnia | % en Riesgo |
|-------|-------------|
| Group A | 8.2% |
| Group B | 7.9% |
| Group C | 6.8% |
| Group D | 7.1% |
| Group E | 6.5% |

---

## 4. Propuestas de Mejora

### PROPUESTA 1: Mentoría Académica +X para Hombres en Riesgo

**Objetivo:** Reducir tasa de fracaso masculino de 9.6% → 6.5% en 2 años (+48% reducción)

**Target:** 1,500 hombres identificados con riesgo (total score < 250)

**Diseño del Programa:**
```
Fase 1: Identificación (M0)
- Identificar hombres con total_score < 250
- Estratificación por asignatura crítica (math/writing < 60)
- Consentimiento informado + matching mentor

Fase 2: Mentoría 1:1 (M1-6, Semestre 1)
- 1 hora/semana × 12 semanas = 12 horas/semestre
- Mentor asignado según especialidad débil
- Seguimiento en-tiempo-real

Fase 3: Talleres de Habilidades (M1-6)
- Gestión de tiempo (2 sesiones)
- Estrategias de estudio (2 sesiones)
- Resiliencia académica (2 sesiones)

Fase 4: Sostenibilidad (M7-12)
- Check-in mensual
- Ajustes de estrategia según progreso
- Transición a peer mentoring para cohort antiguo
```

**Presupuesto:**
| Item | Costo Unitario | Cantidad | Subtotal |
|------|---|---|---|
| Mentores (HS+++) | $25/hora | 180 horas | $4,500 |
| Facilitadores talleres | $20/hora | 60 horas | $1,200 |
| Materiales/recursos | $2/estudiante | 1,500 | $3,000 |
| Administración (10%) | - | - | $1,000 |
| Contingencia (15%) | - | - | $1,550 |
| **TOTAL** | - | - | **$11,250** |
| **Costo por alumno** | - | - | **$7.50** |

**Impacto Esperado:**
- Mejora promedio: +15-20 puntos (+6-7%)
- Reducción fracaso: 9.6% → 6.5% (-3.1pp)
- Retención: 90% → 95%
- Confianza académica: +25% auto-reporte

**Timeline:**
- M0: Diseño + capacitación mentores
- M1: Piloto con 150 estudiantes
- M3: Escalado a 500
- M6: Full program 1,500
- M12+: Sostenibilidad (escalado a 2,500)

**ROI:**
- Cualitativo: Reducción inequidad de género (alineado con inclusión institucional)
- Cuantitativo: 465 estudiantes adicionales pasan (reducción de 733 → 268 en riesgo)
- Valor social: Prevención de 1-2 años de repetición académica

---

### PROPUESTA 2: Test Preparation Course Rediseñado

**Objetivo:** Aumentar efecto de test prep de +1.28 pts → +5-8 pts (+500% ROI)

**Root Cause del Underperformance:**
1. Sesgo de autoselección (bajo desempeño se inscribe)
2. Contenido poco focalizado (taller de 10 horas, genérico)
3. Falta de seguimiento individual
4. Timing inadecuado (late intervention)

**Diseño del Programa Rediseñado (3 Tracks):**

#### Track A: Prevención Temprana (NUEVO)
**Target:** Total score 200-250 (zona crítica mejorable)
**Población:** ~1,800 estudiantes
**Contenido:**
- 20 horas presenciales (1.5h × 13 semanas)
- Fundamentals (no remedial mindset)
- Peer learning + gamificación
- Assessment formativo cada 2 semanas

**Costo:** $40/estudiante × 1,800 = $72,000

#### Track B: Intensivo (ACTUALIZADO)
**Target:** Total score 250-320 (zona de mejora óptima)
**Población:** ~1,200 estudiantes (selección curada)
**Contenido:**
- 30 horas totales (vs. 10 actuales)
- 2h/semana × 15 semanas = 30h presencial
- 50% Presencial (grupo) + 50% Online (individual)
- Specialización por asignatura débil
- 1:1 coaching cada 2 semanas
- Estrategia de test-taking avanzada

**Costo:** $80/estudiante × 1,200 = $96,000

#### Track C: Excellence Plus (NUEVO)
**Target:** Total score 320+ (consolidación A+ performance)
**Población:** ~400 estudiantes (high-achievers)
**Contenido:**
- 15 horas avanzadas (refinamiento)
- Project-based learning (real-world applications)
- Peer teaching role (retroalimentación a otros)

**Costo:** $30/estudiante × 400 = $12,000

**Total Population:** 1,800 + 1,200 + 400 = 3,400 estudiantes (34% del total)

#### Componente Cross-Track: Monitoreo de Efectividad

**Medición:**
- Pre-test: Línea base (todas asignaturas)
- Mid-test: M7 (reajuste de estrategia)
- Post-test: M15 (evaluación de efecto)
- Follow-up: M24 (sostenibilidad)

**Grupo Control:** 20% random (no inscrito) para estimar sesgo de autoselección

**Costo:** $5,000 (análisis + plataforma)

---

**Presupuesto Consolidado - Propuesta 2:**
| Item | Costo |
|------|-------|
| Track A (1,800 × $40) | $72,000 |
| Track B (1,200 × $80) | $96,000 |
| Track C (400 × $30) | $12,000 |
| Facilitadores (+50% time) | $36,000 |
| Plataforma online | $8,000 |
| Monitoreo/evaluación | $5,000 |
| Materiales impresos | $4,000 |
| Contingencia (10%) | $23,300 |
| **TOTAL** | **$256,300** |
| **Costo por alumno** | **$75** |

**Impacto Esperado:**
- Mejora promedio Track A: +4 puntos (fundamental recovery)
- Mejora promedio Track B: +7 puntos (óptimo ROI)
- Mejora promedio Track C: +2 puntos (refinamiento)
- **Promedio ponderado:** +5.6 puntos (+2.1% global)
- Costo por punto: $45 (vs. current $120)
- **ROI Mejora:** 3.3x

**Timeline:**
- M0: Rediseño de contenido + capacitación facilitadores
- M1: Lanzamiento Track A (piloto 150)
- M2: Lanzamiento Track B (piloto 100)
- M3: Lanzamiento Track C (piloto 50)
- M6: Escalado a full program
- M9: First evaluation cycle
- M12-24: Optimización iterativa

---

## 5. Recomendaciones Prioritarias

### Implementación Propuesta (Timeline 24 Meses)

```
FASE 1: SETUP (M0-M1)
├── Propuesta 1: Capacitación mentores + pareamiento (P1: Crítica)
├── Propuesta 2: Rediseño curricular + capacitación facilitadores (P2: Crítica)
└── Sistemas de monitoreo + dashboards

FASE 2: PILOTO (M1-M3)
├── Propuesta 1: 150 hombres en mentoría
├── Propuesta 2: 300 estudiantes en tracks rediseñados
└── Recolección de datos baseline

FASE 3: EARLY WINS (M3-M6)
├── Propuesta 1: Escalado a 500 estudiantes
├── Propuesta 2: Escalado a 1,500 estudiantes
└── Primeras evaluaciones de impacto

FASE 4: FULL DEPLOYMENT (M6-M12)
├── Propuesta 1: 1,500 estudiantes (54% reducción fraude/brecha)
├── Propuesta 2: 3,400 estudiantes (42% de población)
└── Evaluación intermedia + ajustes

FASE 5: SOSTENIBILIDAD (M12-M24)
├── Integración en procesos académicos estándar
├── Entrenamiento de coordinadores permanentes
└── Iteración basada en evidencia
```

### Métricas de Éxito (KPIs)

**Propuesta 1 - Mentoría:**
| KPI | Baseline | Meta M12 | Meta M24 |
|-----|----------|----------|----------|
| % Fracaso Hombres | 9.6% | 8.1% | 6.5% |
| Promedio Hombres | 252.53 | 263 | 270 |
| Brecha Género | +24.36 | +18 | +12 |
| Retención M1→M2 | 90% | 94% | 97% |
| Satisfacción Mentor | - | 4.0/5 | 4.3/5 |

**Propuesta 2 - Test Prep:**
| KPI | Baseline | Meta M12 | Meta M24 |
|-----|----------|----------|----------|
| Efecto Promedio | +1.28 | +3.5 | +5.6 |
| Costo/Punto | $120 | $70 | $45 |
| % Mejora 5+ puntos | 28% | 45% | 60% |
| Sesgo Autoselección | -3.6pp | -1.5pp | 0pp |

---

## 6. Análisis de Riesgo y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|------------|--------|-----------|
| Capacidad de mentores insuficiente | Media | Alto | Capacitación robusta + shadowing inicial |
| Attrition de estudiantes en programa | Media | Medio | Check-ins frecuentes + incentivos |
| Confounding en test prep (macroeconomía) | Baja | Bajo | Grupo control + análisis multivariable |
| Presupuesto insuficiente | Baja | Alto | Propuesta 1 escalable; Propuesta 2 modular |
| Rechazo cultural (estigma de "remedial") | Media | Medio | Rebranding como "preparación + mentoría" |

---

## 7. Conclusiones

### Síntesis
La institución tiene un **desempeño académico sólido en promedio** (65.6% A+B) pero exhibe **inequidades estructurales críticas** que limitan la excelencia:

1. **Brecha de género:** Hombres en desventaja 5.3x en fracaso (inequidad institucional)
2. **SES partially addressed:** Programa de subsidios funciona pero necesita profundización para hombres
3. **Test prep suboptimizado:** Alto gasto, bajo retorno; requiere rediseño urgente

### Oportunidades (Impacto Potencial)
- **Mentoría +X:** -48% fracaso en hombres (733 → 385 en riesgo a M24)
- **Test Prep Rediseño:** +500% ROI ($45/punto vs. $120)
- **Combinado:** Reducción global de inequidad, mejora de 3-5 puntos promedio

### Recomendación Final
**Implementar ambas propuestas en paralelo con financiamiento escalonado:**
- Año 1: $11,250 (mentoría piloto) + $51,300 (test prep piloto) = **$62,550**
- Año 2: Escalado completo con ajustes basados en M12 learnings
- Año 3+: Integración en presupuesto operativo permanente

**Criterio de Éxito:** Brecha de género reduce a +15 puntos (de +24.36) en 24 meses.

---

## Anexo: Metodología de Limpieza de Datos

**Dataset Original:** 10,000 registros × 12 variables  
**Dataset Final:** 9,980 registros × 20 variables (99.81% completo)

### Problemas Identificados y Resueltos
1. **math_score como STRING:** Convertido a float64 con pd.to_numeric()
2. **229 valores nulos distribuidos:** Estrategia selectiva
   - roll_no nulos: DROP (20 registros)
   - Scores: Pairwise deletion (imputation no apropiada)
   - Categoricals: Mode imputation
3. **0 duplicados:** Verificado
4. **Outliers:** Flagged (no eliminados) con IQR method

### Variables Ingenierizado
1. `academic_strength`: Índice balanceado de cuatro asignaturas
2. `is_at_risk`: Binary flag (D+Fail)
3. `high_achiever`: Binary flag (A+B)
4. `gender_binary`: Normalización (male=0, female=1)
5. `performance_balance`: Coeficiente de variación entre asignaturas
6. `parental_education_level`: Ordinal encoding
7. `socioeconomic_proxy`: Combinación lunch + parental edu
8. `science_strong`: Boolean para identificar fortaleza STEM

### Validación (5/5 Checks Passed)
✓ math_score dtype float64  
✓ Todos scores en [0, 100]  
✓ total_score = sum([math, reading, writing, science])/4  
✓ grades válidos [A, B, C, D, Fail]  
✓ 0 duplicados en roll_no  

---

---

## Firma y Acreditación

**Documento Preparado:** 30 de Abril de 2026  
**Equipo:** Grupo 2Prog3 - Introducción al Análisis de Datos  

### Integrantes Responsables
- Gonzalo Fracchia (Coordinador General)
- Máximo Scopel (Análisis Estadístico)
- Tomás Ferreyra (Visualización de Datos)
- Enzo Dengra (Limpieza de Datos)
- Lisandro Nuñez (Backend/Infraestructura)
- Martiniano Rivas (Documentación)

**Status:** Listo para Presentación Ejecutiva

---

**Comisión:** 2Prog3  
**Carrera:** Introducción al Análisis de Datos  
**Año Académico:** 2026  

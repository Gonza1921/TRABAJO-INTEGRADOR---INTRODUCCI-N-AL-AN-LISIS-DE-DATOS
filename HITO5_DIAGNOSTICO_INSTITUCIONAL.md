# Hito 5 — Diagnóstico Institucional y Propuestas de Mejora

**Análisis de Datos Educativos — TPI 2026**

---

## Información del Grupo

| # | Integrante | Rol |
|---|------------|-----|
| 1 | Gonzalo Fracchia | Coordinador General |
| 2 | Máximo Scopel | Análisis Estadístico |
| 3 | Tomás Ferreyra | Visualización de Datos |
| 4 | Enzo Dengra | Limpieza de Datos (ETL) |
| 5 | Lisandro Nuñez | Backend/Infraestructura |
| 6 | Martiniano Rivas | Documentación |

**Comisión:** 2Prog3  
**Carrera:** Introducción al Análisis de Datos  
**Año:** 2026  

---

## Resumen Ejecutivo

Este informe presenta el diagnóstico institucional basado en el análisis de 9,999 registros académicos de estudiantes, evaluando 4 disciplinas (Matemáticas, Lectura, Escritura y Ciencias) a través de 21 variables. Se identifican **3 factores críticos de inequidad** y se proponen **2 intervenciones justificadas** con presupuesto, timeline y métricas de éxito definidas.

---

## Diagnóstico Institucional

### Hallazgo 1: Brecha de Género (CRÍTICO)

Análisis de 9,980 estudiantes con género registrado revela una disparidad estructural significativa:

| Métrica | Mujeres | Hombres | Brecha |
|---------|---------|---------|--------|
| Promedio Total | 276.89 pts | 252.53 pts | +24.36 pts (+9.6%) |
| Tasa Fracaso (D/Fail) | 1.8% | 9.6% | **5.3x más riesgo** |
| % Alto Desempeño | 69.8% | 61.4% | +8.4 pp |

**Desglose por Asignatura:**

| Asignatura | Mujeres | Hombres | Diferencia |
|------------|---------|---------|------------|
| Matemáticas | 66.13 | 48.48 | +17.65 |
| Lectura | 75.29 | 64.58 | +10.71 |
| Escritura | 77.06 | 64.74 | +12.32 |
| Ciencias | 75.83 | 55.69 | +20.14 |

**Análisis:** La brecha es consistente en todas las asignaturas y se agrava en Ciencias (+20.14 pts) y Matemáticas (+17.65 pts), contradiciendo estereotipos tradicionales. La tasa de fracaso 5.3x en hombres indica un problema sistémico de engagement y retención, no de capacidad.

---

### Hallazgo 2: Inequidad Socioeconómica

| Métrica | Sin Subsidio | Con Subsidio | Brecha |
|---------|-------------|--------------|--------|
| Promedio Total | 263.18 pts | 270.81 pts | +7.63 pts (+2.8%) |
| Tasa Fracaso | 8.8% | 5.9% | 1.5x más riesgo |
| Población | 3,549 (35.5%) | 6,426 (64.5%) | — |

**Intersección Género × SES:**

| Segmento | Tasa Fracaso |
|----------|-------------|
| Hombres sin subsidio | **13.5%** (CRÍTICO) |
| Hombres con subsidio | 5.1% |
| Mujeres sin subsidio | 2.3% |
| Mujeres con subsidio | 1.2% |

**Análisis:** El programa de subsidios mitiga parcialmente la inequidad, pero los hombres de bajos recursos tienen 11.3x más probabilidad de fracasar que las mujeres con subsidio. Esto sugiere que el subsidio solo no es suficiente — se necesita intervención complementaria.

---

### Hallazgo 3: Test Preparation — Efecto Paradójico

| Asignatura | Sin Prep | Con Prep | Dif |
|------------|----------|----------|-----|
| Matemáticas | 65.05 | 64.93 | -0.12 |
| Lectura | 68.30 | 68.50 | +0.20 |
| Escritura | 65.63 | 66.85 | **+1.22** |
| Ciencias | 68.50 | 68.48 | -0.02 |
| **Total** | **267.48** | **268.76** | **+1.28** |

Tasa A+B: Sin prep 61.9% vs Con prep 59.4% (correlación NEGATIVA)

**Análisis de Causa Raíz:** Sesgo de autoselección — estudiantes con bajo rendimiento se inscriben en test prep, generando una correlación espuria negativa. El efecto real de +1.28 pts es insuficiente para justificar la inversión actual.

---

### Hallazgo 4: Educación Parental — Relación No Lineal

| Nivel Educativo | Promedio | Población | Tasa Fracaso |
|----------------|----------|-----------|-------------|
| Master's degree | 258.39 | 711 (7.1%) | 11.5% |
| Bachelor's degree | 272.26 | 1,361 (13.7%) | 4.8% |
| Associate's degree | 269.74 | 1,905 (19.1%) | 6.2% |
| Some college | 267.21 | 2,272 (22.8%) | 7.3% |
| High school | 263.92 | 1,986 (19.9%) | 8.1% |
| Some high school | 266.91 | 1,742 (17.5%) | 9.4% |

**Paradoja:** Master's degree presenta el peor desempeño (11.5% fracaso). Esto sugiere factores confundentes como estándares parentales elevados o diferencias en el tipo de posgrado.

---

### Hallazgo 5: Perfil de Estudiante en Riesgo

**Población en Riesgo:** 733 estudiantes (7.3% del total), definidos por calificación D o Fail.

**Perfil Característico:**
- Género: 74.6% hombres
- Educación parental: 62% ≤ high school
- Subsidio: 58.1% sin subsidio
- Test prep: solo 31.5% completó curso

**Distribución por Grupo Étnico:** Homogénea (6.5%–8.2%), sin disparidad significativa.

---

## Propuestas de Mejora Justificadas

### Propuesta 1: Programa de Mentoría Académica +X para Hombres en Riesgo

**Justificación:** El Hallazgo 1 demuestra que los hombres tienen 5.3x más riesgo de fracaso, y el Hallazgo 2 muestra que los hombres sin subsidio alcanzan 13.5% de fracaso. La mentoría 1:1 aborda la causa raíz identificada: falta de engagement y modelos académicos.

**Objetivo:** Reducir tasa de fracaso masculino de 9.6% → 6.5% en 24 meses.

**Componentes:**

| Componente | Descripción | Costo |
|------------|-------------|-------|
| Mentoría 1:1 | 12h/semestre por estudiante | $4,500 |
| Talleres habilidades | 6 sesiones (time mgmt, estudio, resiliencia) | $1,200 |
| Materiales | Recursos de apoyo | $3,000 |
| Administración | Coordinación y monitoreo | $2,550 |

**Presupuesto Total:** $11,250  
**Costo por Estudiante:** $7.50  
**Cobertura:** 1,500 estudiantes en riesgo  

**Métricas de Éxito:**

| KPI | Línea Base | Meta M12 | Meta M24 |
|-----|-----------|----------|----------|
| Fracaso hombres | 9.6% | 8.1% | 6.5% |
| Promedio hombres | 252.5 pts | 263 pts | 270 pts |
| Brecha género | +24.4 pts | +18 pts | +12 pts |
| Retención | 90% | 94% | 97% |

---

### Propuesta 2: Rediseño del Curso de Preparación Académica (Test Prep)

**Justificación:** El Hallazgo 3 evidencia que el programa actual genera solo +1.28 pts de mejora con una inversión significativa, y el Hallazgo 4 muestra que estudiantes con padres de menor educación tienen hasta 2.4x más riesgo. Un rediseño focalizado maximiza el ROI.

**Objetivo:** Aumentar efecto de +1.28 pts → +5.6 pts (+337% mejora).

**Modelo de 3 Tracks:**

| Track | Target | Población | Horas | Costo/Est | Costo Total |
|-------|--------|-----------|-------|-----------|-------------|
| A — Prevención | Score 200-250 | 1,800 | 20h presencial | $40 | $72,000 |
| B — Intensivo | Score 250-320 | 1,200 | 30h mixto | $80 | $96,000 |
| C — Excellence | Score 320+ | 400 | 15h avanzado | $30 | $12,000 |

**Presupuesto Consolidado:** $256,300  
**Cobertura:** 3,400 estudiantes (34% de la población)  
**Costo por Estudiante:** $75  

**Métricas de Éxito:**

| KPI | Línea Base | Meta M12 | Meta M24 |
|-----|-----------|----------|----------|
| Efecto promedio | +1.28 pts | +3.5 pts | +5.6 pts |
| Costo por punto | $120 | $70 | $45 |
| Estudiantes con mejora 5+ pts | 28% | 45% | 60% |

**Componente de Monitoreo:** Pre-test, mid-test (M7), post-test (M15), follow-up (M24) con grupo control del 20% para controlar sesgo de autoselección.

---

## Plan de Implementación (24 Meses)

| Fase | Período | Propuesta 1 | Propuesta 2 | Inversión |
|------|---------|-------------|-------------|-----------|
| Setup | M0-M1 | Capacitación mentores | Rediseño curricular | $5,000 |
| Piloto | M1-M3 | 150 estudiantes | 300 estudiantes (3 tracks) | $28,500 |
| Early Wins | M3-M6 | 500 estudiantes | 1,500 estudiantes | $45,000 |
| Full Deployment | M6-M12 | 1,500 estudiantes | 3,400 estudiantes | $133,000 |
| Sostenibilidad | M12-M24 | Integración permanente | Optimización iterativa | $75,000 |

**Inversión Total Estimada:** $286,550 (Año 1: $62,550 + Año 2: $224,000)

---

## Análisis de Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|------------|---------|------------|
| Capacidad mentores insuficiente | Media | Alto | Capacitación + shadowing |
| Attrition estudiantes | Media | Medio | Incentivos + check-ins |
| Confounding test prep | Baja | Bajo | Grupo control 20% |
| Presupuesto insuficiente | Baja | Alto | Implementación modular |
| Estigma "remedial" | Media | Medio | Rebranding positivo |

---

## Conclusiones

1. **Diagnóstico:** La institución tiene desempeño sólido (65.6% A+B) pero inequidades estructurales que requieren intervención inmediata, especialmente la brecha de género (5.3x en fracaso).

2. **Propuestas:** Mentoría +X ($11,250) y Test Prep Rediseñado ($256,300) abordan las causas raíz identificadas con presupuestos y timelines realistas.

3. **Impacto esperado:** Reducción de brecha de género de +24.4 pts a +12 pts en 24 meses, mejora de 3-5 pts en promedio global.

4. **Recomendación:** Implementar ambas propuestas en paralelo con financiamiento escalonado, evaluación longitudinal, y ajustes basados en evidencia en M12.

---

## Referencias

- Dataset: Student_performance_CLEANED.csv (9,999 registros, 21 variables)
- Dashboard interactivo: app.py (Streamlit, 4 tabs, filtros dinámicos)
- Dashboard Grafana: dashboard_tpi_grafana.json (8 paneles)
- Informe completo: informe_final.md

---

**Comisión:** 2Prog3 | **Carrera:** Introducción al Análisis de Datos | **Año:** 2026

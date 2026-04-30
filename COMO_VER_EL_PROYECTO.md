# 🎓 CÓMO VER EL PROYECTO COMPLETO - GUÍA RÁPIDA

## Opción 1: Dashboard Interactivo (LO MEJOR) 🎯

### Paso 1: Abre PowerShell o CMD
Presiona `Windows + R`, escribe `cmd` o `powershell` y presiona Enter.

### Paso 2: Navega a la carpeta
```bash
cd "C:\Users\gonzi\Desktop\TRABAJO INTEGRADOR - INTRODUCCIÓN AL ANÁLISIS DE DATOS"
```

### Paso 3: Ejecuta el dashboard
```bash
streamlit run app.py
```

### Paso 4: Se abrirá automáticamente en tu navegador
- URL: `http://localhost:8501`
- Verás 4 pestañas: Dashboard Ejecutivo | Análisis Detallado | Segmentación | Insights

### Para VER INFORMACIÓN DEL GRUPO:
- En la barra izquierda (sidebar)
- Presiona "👥 Información del Grupo"
- Verás Comisión 2Prog3 y los 6 integrantes

### Para CERRAR:
- Presiona `Ctrl+C` en PowerShell/CMD

---

## Opción 2: Leer el Informe Ejecutivo 📄

### Archivo:
```
C:\Users\gonzi\Desktop\TRABAJO INTEGRADOR - INTRODUCCIÓN AL ANÁLISIS DE DATOS\informe_final.md
```

### Cómo abrirlo:
1. **Con Bloc de Notas:** Click derecho → Abrir con → Bloc de Notas
2. **Con VS Code:** Click derecho → Abrir con → Visual Studio Code (mejor formato)
3. **Con navegador:** Arrastrar el archivo a Chrome/Firefox

### Qué encontrarás:
- **PORTADA:** Información completa del grupo (Gonzalo, Máximo, Tomás, Enzo, Lisandro, Martiniano)
- **5 HALLAZGOS:** Brecha género, SES gap, test prep, educación parental, perfil de riesgo
- **2 PROPUESTAS:** Mentoría +X ($11.25K), Test Prep Rediseño ($256.3K)
- **TIMELINE:** Plan de implementación 24 meses
- **FIRMA:** Al final con todos los integrantes

---

## Opción 3: Ver el Código y Análisis (Jupyter Notebook) 🔬

### Archivo:
```
C:\Users\gonzi\Desktop\TRABAJO INTEGRADOR - INTRODUCCIÓN AL ANÁLISIS DE DATOS\Analisis_TPI_Completo.ipynb
```

### Opción A: Con Jupyter Lab (RECOMENDADO)
```bash
# En PowerShell, en la misma carpeta:
jupyter lab
```
- Se abrirá en navegador
- Busca "Analisis_TPI_Completo.ipynb" y click
- Verás todo el código, gráficos y análisis paso a paso

### Opción B: Con Jupyter Notebook
```bash
# En PowerShell, en la misma carpeta:
jupyter notebook
```
- Selecciona "Analisis_TPI_Completo.ipynb"

### Opción C: Con Visual Studio Code
- Abre VS Code
- Arrastra el archivo al VS Code
- Necesitas extensión "Jupyter" instalada

### En la PRIMERA CELDA:
- Verás la portada con comisión 2Prog3 y todos los 6 integrantes

---

## Opción 4: Guía General (README) 📖

### Archivo:
```
C:\Users\gonzi\Desktop\TRABAJO INTEGRADOR - INTRODUCCIÓN AL ANÁLISIS DE DATOS\README.md
```

### Qué contiene:
- Información completa del grupo con roles
- Descripción del proyecto
- 5 hallazgos principales (resumen)
- 2 propuestas de mejora (resumen)
- Estructura del proyecto
- Guía por rol (quién debe revisar qué)
- Estadísticas clave

---

## Mi Recomendación 💡

### Si tienes poco tiempo (10 minutos):
1. Abre `README.md` → Lee sección "Hallazgos Principales"
2. Listo! Entiendes el proyecto

### Si tienes 30 minutos:
1. Abre `README.md` → Lee todo
2. Abre `informe_final.md` → Lee Portada + Conclusiones
3. Ves cómo se divide el trabajo entre integrantes

### Si tienes 1 hora:
1. Ejecuta el dashboard: `streamlit run app.py`
2. Explora las 4 pestañas
3. Prueba los filtros interactivos
4. Descarga CSVs de segmentos

### Si tienes más tiempo (completo):
1. Dashboard interactivo
2. Lee README.md completo
3. Lee informe_final.md completo
4. Abre Jupyter Notebook y sigue el análisis paso a paso

---

## 📍 Ubicación de Información del Grupo

### Portada/Inicio
- **README.md** - Sección inicial "Información del Grupo"
- **informe_final.md** - PORTADA EJECUTIVA (tabla con roles)
- **app.py** - Título de página incluye "2Prog3"
- **Notebook** - Primera celda Markdown

### Durante el uso
- **Dashboard** - Presiona "👥 Información del Grupo" en sidebar
- **README** - Cada sección indica quién revisar (guía por rol)

### Al cierre
- **informe_final.md** - "Firma y Acreditación" con todos los 6 nombres
- **app.py** - Footer incluye "Grupo 2Prog3" y todos los integrantes

---

## 🔗 Estructura de Carpetas

```
TRABAJO INTEGRADOR/
├── README.md                          ← GUÍA GENERAL (EMPEZAR AQUÍ)
├── informe_final.md                   ← INFORME EJECUTIVO
├── Analisis_TPI_Completo.ipynb       ← ANÁLISIS TÉCNICO
├── app.py                             ← DASHBOARD (ejecutar con streamlit)
├── VERIFICACION_GRUPO.md              ← Checklist de actualizaciones
│
├── Student_performance_CLEANED.csv    ← Datos limpios
├── Estudiantes_En_Riesgo.csv         ← Segmento: en riesgo
├── Estudiantes_Alto_Desempeno.csv    ← Segmento: alto rendimiento
│
└── Visualizations/
    ├── 01_grafico_distribucion_genero.png
    ├── 02_grafico_correlaciones_heatmap.png
    ├── 03_grafico_subsidio_impacto.png
    ├── 04_grafico_educacion_parental.png
    ├── 05_grafico_test_prep_efectividad.png
    └── 06_grafico_distribucion_scores.png
```

---

## 👥 Información del Grupo - RESUMEN

| Integrante | Rol | Revisar Primero |
|---|---|---|
| Gonzalo Fracchia | Coordinador General | README.md + informe_final.md |
| Máximo Scopel | Análisis Estadístico | informe_final.md (Hallazgos) + Notebook |
| Tomás Ferreyra | Visualización | Gráficos PNG + Dashboard (Tab 1-2) |
| Enzo Dengra | ETL/Limpieza | Notebook (Celdas 1-3) + VERIFICACION_GRUPO.md |
| Lisandro Nuñez | Backend | app.py + informe_final.md (Implementación) |
| Martiniano Rivas | Documentación | README.md + informe_final.md (Cualidad) |

**Comisión:** `2Prog3`

---

## ❓ Preguntas Frecuentes

### P: ¿Necesito instalar algo?
**R:** Solo si quieres ejecutar el dashboard o notebook. Para leer documentos, no.

### P: ¿Dónde están los datos?
**R:** `Student_performance_CLEANED.csv` (9,999 estudiantes, 21 variables)

### P: ¿Cuántos gráficos hay?
**R:** 6 PNG estáticos en el notebook + gráficos interactivos en el dashboard

### P: ¿Puedo descargar datos filtrados?
**R:** Sí, en el dashboard pestaña "Segmentación" hay botones de descarga CSV

### P: ¿Cuál es la conclusión principal?
**R:** Inequidad de género crítica (hombres 5.3x más riesgo). Se proponen 2 soluciones basadas en evidencia.

---

**¡Listo! Ahora sabes cómo ver todo el proyecto.** 🚀

Comienza por: **README.md o Dashboard** según tu preferencia.

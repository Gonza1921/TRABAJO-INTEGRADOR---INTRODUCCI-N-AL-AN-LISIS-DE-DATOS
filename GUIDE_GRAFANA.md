# Guía de Instalación y Configuración — Grafana + SQLite

Esta guía explica cómo visualizar el análisis del TPI en Grafana usando la base de datos SQLite generada a partir del dataset de estudiantes.

---

## 1. Prerrequisitos

- **Grafana** (v9+ recomendado)
- **Plugin SQLite para Grafana** (`frser-sqlite-datasource`)
- **academico.db** (ya generado en el proyecto)

---

## 2. Instalar Grafana

### Windows

```powershell
# Descargar desde:
# https://grafana.com/grafana/download?platform=windows
# Ejecutar el instalador MSI
```

### Linux (Ubuntu/Debian)

```bash
sudo apt-get install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install grafana
sudo systemctl start grafana-server
```

### macOS

```bash
brew install grafana
brew services start grafana
```

---

## 3. Instalar Plugin SQLite

Acceder a la consola de Grafana y ejecutar:

```bash
# Ruta típica de la CLI de Grafana
# Windows:
grafana-cli plugins install frser-sqlite-datasource

# Linux/macOS:
sudo grafana-cli plugins install frser-sqlite-datasource
```

Luego **reiniciar Grafana**:

```bash
# Windows: reiniciar servicio desde Services.msc
# Linux: sudo systemctl restart grafana-server
# macOS: brew services restart grafana
```

---

## 4. Configurar la Fuente de Datos SQLite

1. Abrir Grafana en el navegador: `http://localhost:3000`
2. Login por defecto: `admin` / `admin`
3. Ir a **Configuration → Data Sources → Add data source**
4. Buscar y seleccionar **SQLite**
5. Configurar:

| Campo                | Valor                                                              |
|----------------------|--------------------------------------------------------------------|
| Name                 | `TPI SQLite` (o el que prefieras)                                  |
| File Path            | Ruta absoluta a `academico.db`                                     |

   **Ejemplo de ruta (Windows):**
   ```
   C:\Users\tfutn\Documents\TUP 2026 2°\ANALISIS DE DATOS\Parciales\Parcial 2- hito 3 y 4\TRABAJO-INTEGRADOR---INTRODUCCI-N-AL-AN-LISIS-DE-DATOS\academico.db
   ```

6. Hacer clic en **Save & Test** — debería mostrar "Database connection OK"

---

## 5. Importar el Dashboard

1. Ir a **+ → Import** en el menú lateral
2. Subir el archivo `dashboard_tpi_grafana.json`
3. En el campo **TPI SQLite** (o el nombre que le diste a la fuente de datos)
4. Hacer clic en **Import**

---

## 6. Verificar el Dashboard

El dashboard importado contiene 9 paneles:

| #  | Panel                              | Tipo     | Descripción                                      |
|----|-----------------------------------|----------|--------------------------------------------------|
| 1  | Promedio Total Score              | Stat     | Promedio general del puntaje total               |
| 2  | % Alto Desempeño (A+B)            | Stat     | Porcentaje de estudiantes con calificación A o B |
| 3  | % Estudiantes en Riesgo           | Stat     | Porcentaje de estudiantes en riesgo              |
| 4  | Brecha de Género                  | Stat     | Diferencia de promedio (mujeres - hombres)       |
| 5  | Distribución por Género           | Bar      | Calificaciones apiladas por género               |
| 6  | Impacto del Subsidio              | Bar      | Promedio por materia con/sin subsidio            |
| 7  | Efectividad Test Prep             | Bar      | Promedio por materia con/sin preparación         |
| 8  | Score por Educación Parental      | Bar      | Promedio según nivel educativo de los padres     |
| 9  | Estadísticas por Grupo Étnico     | Table    | Métricas detalladas por grupo étnico             |

---

## 7. Solución de Problemas

| Problema                        | Posible Causa                             | Solución                                                     |
|---------------------------------|-------------------------------------------|--------------------------------------------------------------|
| "Plugin not found"              | Plugin SQLite no instalado                | Ejecutar `grafana-cli plugins install frser-sqlite-datasource` |
| "Database not found"            | Ruta incorrecta a academico.db            | Usar ruta absoluta correcta                                  |
| "Query error"                   | SQL inválido para la versión del plugin   | Verificar que las tablas existen con `PRAGMA table_info(estudiantes)` |
| Paneles sin datos               | Plugin no soporta ciertos formatos        | Usar formato `table` en las queries                          |
| "Access denied" a academico.db  | Permisos de archivo                       | Dar permisos de lectura al usuario de Grafana                |

---

## 8. Notas Adicionales

- El dashboard se refresca automáticamente cada 30 segundos.
- Todos los paneles usan SQL directo contra la tabla `estudiantes`.
- El datasource usa el plugin `frser-sqlite-datasource`.
- El dashboard original (Streamlit) se mantiene intacto — ambos pueden coexistir.

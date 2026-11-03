# Fase 1: Arquitectura, Inversión de Datos y Python Moderno (Días 1 al 7)

## Objetivo

Sentar las bases del código, entender el por qué del stack técnico moderno y construir un motor de ingesta de datos robusto y validado.

## Stack Tecnológico

- **Lenguaje:** Python 3.12+
- **Gestor de dependencias:** `uv`
- **Validación de esquemas:** `Pydantic v2`
- **Cliente HTTP:** `httpx`

## El Porqué de Cada Elección (Justificación Técnica)

- **Python 3.12+:** El estándar indiscutido en Data Engineering y Backend moderno por su ecosistema masivo y velocidad de desarrollo.
- **`uv`:** Reemplaza a `pip` y `poetry`. Escrito en Rust, gestiona entornos y dependencias de forma ultrarrápida, demostrando actualización en tooling.
- **Pydantic v2:** Regla de oro en datos (_basura entra, basura sale_). Valida los esquemas en tiempo de ejecución con velocidad cercana a C, evitando que cambios en APIs externas rompan el pipeline de forma silenciosa.
- **`httpx`:** Cliente HTTP moderno que soporta llamadas asíncronas y tipado estricto, superando al clásico `requests`.

## Tareas Paso a Paso (Estructura Modular)

1. **Inicialización del entorno:**
   - Instalar `uv` y crear un proyecto nuevo (`uv init --app`).
     |- install: `curl -LsSf https://astral.sh/uv/install.sh | sh`
     |- check: `uv --version`
   - Instalar versión de Python fijada (`uv python pin 3.12`).
   - Instalar dependencias core (`uv add httpx pydantic`).
   - Configurar la estructura modular del proyecto (`src/` con `models.py`, `extractor.py`, `main.py` y carpeta `tests/`).

2. **Definición de Modelos (`src/models.py`):**
   - Elegir una API pública y estable (por ejemplo, JSONPlaceholder para datos de prueba).
   - Escribir los modelos Pydantic estrictos (`BaseModel`, `Field`) que tipifiquen y validen la estructura de los datos entrantes.

3. **Construcción del Extractor (`src/extractor.py`):**
   - Desarrollar la lógica de llamada HTTP con manejo de errores y códigos de estado usando `httpx`.
   - Implementar funciones limpias que devuelvan datos listos para validar.

4. **Orquestación Principal (`src/main.py`):**
   - Unir el extractor y los modelos para ejecutar el flujo completo de ingesta y validación con logs claros en consola.

## Métrica de Éxito de la Fase

- Un script modular en Python que extrae datos de una API externa, los valida mediante esquemas estrictos de Pydantic y los procesa localmente sin errores.

---

---

---

# Explicacion

## Que es ETL

**ETL** significa **Extract, Transform, Load** (en español: **Extracción, Transformación y Carga**).

Es un proceso fundamental en la ingeniería y gestión de datos que se utiliza para mover datos desde diferentes fuentes de origen, prepararlos para su análisis y almacenarlos en un destino final (como un Data Warehouse, una base de datos o almacenamiento en la nube).

Sus tres etapas principales son:

1. **Extracción (Extract):** Se obtienen o recopilan los datos crudos desde diversas fuentes externas (como APIs, bases de datos transaccionales, archivos CSV, sistemas CRM, etc.). En nuestro proyecto, esto lo hace el archivo `extractor.py` consumiendo una API.
2. **Transformación (Transform):** Los datos extraídos se limpian, filtran, validan y estructuran según las reglas de negocio necesarias. Aquí es donde entra la validación estricta de esquemas (como hicimos con **Pydantic**) para asegurar que "lo que entra" tenga la calidad correcta y descartar datos corruptos o malformados.
3. **Carga (Load):** Finalmente, los datos ya limpios y validados se escriben y almacenan en el sistema de destino (en nuestro caso, avanzaremos luego hacia AWS S3 o bases de datos relacionales).

En resumen, es la tubería (_pipeline_) estándar para automatizar el flujo de información en cualquier arquitectura de datos moderna.

```
cloud-pulse-etl/
├── .gitignore # Excluye del repo los archivos .html y fase.md
├── .python-version # Fija la versión de Python en 3.12 para uv
├── pyproject.toml # Metadatos, dependencias (httpx, pydantic) y script del proyecto
├── uv.lock # Lockfile con versiones exactas resueltas por uv
├── README.md # Resumen ejecutivo: qué es el proyecto y qué problema resuelve
├── fase1_ingesta.md # Plan Fase 1: arquitectura e ingesta con Pydantic + httpx
├── fase2_almacenamiento.md # Plan Fase 2: almacenamiento en AWS S3 y PostgreSQL/RDS
├── fase3_api_docker.md # Plan Fase 3: API con FastAPI y contenedores Docker
├── fase4_portfolio_cv.md # Plan Fase 4: despliegue cloud y portfolio para reclutadores
├── pipeline_flow.html # Diagrama visual de la arquitectura ETL de la Fase 1
├── src/ # Código fuente del pipeline ETL
│ ├── main.py # Orquesta el pipeline: extrae, valida e imprime registros
│ ├── extractor.py # Cliente httpx que consulta la API externa de posts
│ ├── models.py # Modelos Pydantic que validan el esquema de los datos
│ └── cloud_pulse_etl/
│ └── init.py # Punto de entrada del paquete/script cloud-pulse-etl
├── tests/ # Carpeta para pruebas unitarias (actualmente vacía)
└── .venv/ # Entorno virtual local con las dependencias instaladas
```

## Que es ELT

**Extract, Load, Transform** / **Extracción, Carga y Transformación**

### ¿En qué se diferencia de ETL?

La diferencia clave está en **dónde** se realiza la transformación (la limpieza y validación de los datos):

1. **ETL (Tradicional):** Primero extraes, luego transformas (validas y limpias) en un servidor intermediario, y finalmente cargas los datos limpios en el destino final. Es ideal cuando el destino tiene capacidad de procesamiento limitada.
2. **ELT (Moderno):** Primero extraes los datos y los **cargas directamente** en bruto (_raw_) en el destino final (por ejemplo, un Data Warehouse en la nube con mucha potencia de cómputo, como Snowflake, BigQuery o Amazon Redshift), y **luego los transformas** dentro de ese mismo sistema.

### ¿Por qué se usa tanto ELT hoy en día?

Con la llegada de la nube y almacenamiento/procesamiento súper económico y veloz, ELT se volvió el estándar en muchas arquitecturas modernas, ya que te permite guardar primero todo el historial sin perder información cruda (_raw data_) y transformar los datos según las necesidades del negocio de forma flexible después.

## Resumen por capas

| Capa          | Elementos                                | Función                                        |
| ------------- | ---------------------------------------- | ---------------------------------------------- |
| Documentación | README, fase1-4                          | Explican el objetivo y las fases del proyecto  |
| Código ETL    | src/\*.py                                | Extracción, validación y orquestación de datos |
| Configuración | pyproject.toml, uv.lock, .python-version | Gestión de dependencias y entorno              |
| Pruebas       | tests/                                   | Espacio reservado para tests                   |

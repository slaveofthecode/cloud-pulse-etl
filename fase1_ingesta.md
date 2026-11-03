# Fase 1: Arquitectura, Inversión de Datos y Python Moderno (Días 1 al 7)

## Objetivo
Sentar las bases del código, entender el por qué del stack técnico moderno y construir un motor de ingesta de datos robusto y validado.

## Stack Tecnológico
* **Lenguaje:** Python 3.12+
* **Gestor de dependencias:** `uv`
* **Validación de esquemas:** `Pydantic v2`
* **Cliente HTTP:** `httpx`

## El Porqué de Cada Elección (Justificación Técnica)
* **Python 3.12+:** El estándar indiscutido en Data Engineering y Backend moderno por su ecosistema masivo y velocidad de desarrollo.
* **`uv`:** Reemplaza a `pip` y `poetry`. Escrito en Rust, gestiona entornos y dependencias de forma ultrarrápida, demostrando actualización en tooling.
* **Pydantic v2:** Regla de oro en datos (*basura entra, basura sale*). Valida los esquemas en tiempo de ejecución con velocidad cercana a C, evitando que cambios en APIs externas rompan el pipeline de forma silenciosa.
* **`httpx`:** Cliente HTTP moderno que soporta llamadas asíncronas y tipado estricto, superando al clásico `requests`.

## Tareas Paso a Paso
1. **Inicialización del entorno:**
   * Instalar `uv` y crear un proyecto nuevo (`uv init stream-lake-core`).
   * Configurar el entorno virtual y la estructura modular del proyecto (`src/`, `tests/`).
2. **Definición de Modelos (Pydantic):**
   * Elegir una API pública y estable (por ejemplo, datos financieros públicos o de transporte).
   * Escribir los modelos Pydantic estrictos que tipifiquen y validen la estructura de los datos entrantes.
3. **Construcción del Extractor (`extractor.py`):**
   * Desarrollar la lógica de llamada HTTP con reintentos automáticos ante fallas de red usando `httpx`.
   * Implementar manejo de excepciones controlado para logs limpios.

## Métrica de Éxito de la Fase
* Un script funcional en Python que extrae datos de una API externa, los valida mediante esquemas estrictos de Pydantic y los imprime/serializa localmente sin errores.
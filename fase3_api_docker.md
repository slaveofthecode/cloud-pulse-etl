# Fase 3: Exposición de Datos (FastAPI) y Contenedorización (Días 15 al 21)

## Objetivo
Convertir tu pipeline de datos en un producto consumible mediante una API de alto rendimiento y empaquetar toda la solución para garantizar portabilidad absoluta en producción.

## Stack Tecnológico
* **Framework Web / API:** FastAPI + Uvicorn
* **Contenedorización:** Docker & Docker Compose

## El Porqué de Cada Elección (Justificación Técnica)
* **FastAPI:** El rey indiscutido para APIs de datos y microservicios en Python. Es asíncrono nativo (Starlette), valida tipos automáticamente usando Pydantic (integrándose de forma transparente con la Fase 1) y genera documentación interactiva con Swagger UI por defecto.
* **Docker:** El estándar de la industria para eliminar el problema de *"en mi máquina funciona"*. Un desarrollador senior debe garantizar que el software corra idénticamente en local, staging y producción.

## Tareas Paso a Paso
1. **Desarrollo de Endpoints con FastAPI:**
   * Crear rutas (`/metrics`, `/summary`, `/healthz`) que consulten la base de datos PostgreSQL y devuelvan las métricas procesadas del pipeline.
   * Aplicar inyección de dependencias para la conexión a la base de datos.
2. **Creación del Dockerfile:**
   * Escribir un `Dockerfile` multi-stage optimizado para aplicaciones Python utilizando imágenes ligeras y gestionando dependencias con `uv`.
3. **Orquestación con Docker Compose:**
   * Configurar un archivo `docker-compose.yml` que levante de forma simultánea la API de FastAPI y la base de datos PostgreSQL conectadas en una red interna aislada.

## Métrica de Éxito de la Fase
* Levantar el sistema completo ejecutando un único comando (`docker compose up`), pudiendo consultar la documentación interactiva en `http://localhost:8000/docs` y obtener respuestas de la API consultando datos reales.
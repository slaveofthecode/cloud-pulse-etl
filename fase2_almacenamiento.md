# Fase 2: Almacenamiento Cloud y Arquitectura de Datos (Días 8 al 14)

## Objetivo
Perderle el miedo a AWS estructurando un almacenamiento empresarial híbrido: un Data Lake en crudo (S3) y una base de datos relacional transaccional optimizada (PostgreSQL en RDS).

## Stack Tecnológico
* **Cloud Storage (Data Lake):** AWS S3
* **Base de Datos Relacional:** AWS RDS (PostgreSQL) / PostgreSQL local con Docker para pruebas
* **SDK Cloud:** `boto3`
* **ORM / Conectividad:** `SQLAlchemy` o `SQLModel`

## El Porqué de Cada Elección (Justificación Técnica)
* **AWS S3 (Capa Bronze/Silver):** En arquitectura de datos moderna, nunca se guarda el dato procesado directamente; se almacena primero el archivo en crudo (formato JSON lines o Parquet) en S3. Si el procesamiento falla o cambia la lógica de negocio, se re-procesa directamente desde S3 sin perder el dato histórico original.
* **AWS RDS PostgreSQL (Capa Gold):** La base de datos relacional más solicitada del mercado. Servir datos procesados desde Postgres a una API es un requisito corporativo estándar.
* **`boto3`:** El SDK oficial de Python para interactuar con AWS, habilidad obligatoria para cualquier ingeniero de backend o datos.

## Tareas Paso a Paso
1. **Configuración de AWS S3:**
   * Crear un bucket privado en S3 mediante la consola de AWS (afianzando los conceptos del curso de certificación).
   * Configurar credenciales seguras de AWS localmente mediante perfiles IAM de menor privilegio.
2. **Automatización de Subida con `boto3`:**
   * Escribir un módulo de carga (`loader_s3.py`) que tome el JSON validado en la Fase 1 y lo suba a S3 particionado por fecha (`/raw/year=YYYY/month=MM/day=DD/data.json`).
3. **Conexión a Base de Datos Relacional:**
   * Levantar un contenedor local de PostgreSQL o configurar una instancia RDS.
   * Diseñar el esquema relacional para guardar los agregados limpios o métricas calculadas a partir de la ingesta.

## Métrica de Éxito de la Fase
* Un pipeline automatizado donde los datos extraídos en la Fase 1 se guardan exitosamente particionados en S3 y sus resúmenes se persisten en PostgreSQL.
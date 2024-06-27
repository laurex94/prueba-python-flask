# Prueba Python - Flask

Este proyecto es una aplicación web simple desarrollada con Flask. La aplicación permite gestionar saludos y almacenarlos en una base de datos PostgreSQL.

## Estructura de Directorios

- **app/**: Contiene los módulos de la aplicación.
  - **greeting/**: Módulo para gestionar saludos y sus rutas.
  - **main/**: Módulo principal de la aplicación.
  - **models/**: Contiene los modelos de base de datos.
  - **__init__.py**: Archivo principal de la aplicación. Contiene la creación de la aplicación y la configuración de la base de datos.

- **Dockerfile**: Archivo para crear la imagen Docker de la aplicación.

- **config.py**: Archivo de configuración de la aplicación.

- **docker-compose.yaml**: Archivo para orquestar contenedores Docker.

- **requirements.txt**: Archivo que lista las dependencias de Python necesarias para la aplicación.

## Configuración del Entorno de Desarrollo

1. Clonar este repositorio.
2. cambiar .env.example a .env

## Ejecución de la Aplicación

1. Ejecutar `docker-compose up` para orquestar los contenedores Docker.

2. Acceder a la aplicación desde un navegador web en [http://localhost:5000/](http://localhost:5000/).

### Pruebas

A continuación se detallan ejemplos de cómo realizar pruebas en la aplicación:

1. **Obtener todos los saludos:**
   - **Método:** GET
   - **URL:** `http://localhost:5000/saludos`

2. **Crear un nuevo saludo con mensaje "Buenos días":**
   - **Método:** POST
   - **URL:** `http://localhost:5000/saludos`
   - **Body:** JSON (`{"mensaje": "Buenos días"}`)

3. **Obtener el saludo con ID:**
   - **Método:** GET
   - **URL:** `http://localhost:5000/saludos/1`

4. **Abrir aplicación en navegador:**
   - **URL:** `http://localhost:5000/`

5. **Abrir endpoint de test en navegador:**
    - **URL:** `http://localhost:5000/test`

Para hacer el test de forma automática, se puede ejecutar el siguiente comando:
   1. **Abrir terminal de la aplicación deentro del contenedor:**
      - **Comando:** `docker exec -it nombre-container bash`
   ```bash
   pytest
   ```



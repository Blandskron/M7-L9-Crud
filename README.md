# Proyecto Django: Link Manager

Este proyecto es una aplicación Django básica que permite gestionar enlaces usando operaciones CRUD (Crear, Leer, Actualizar y Eliminar). A continuación se describen los pasos para configurar y ejecutar este proyecto.

## Estructura del Proyecto

1. **Creación del Proyecto y la Aplicación:**
   - Proyecto Django creado con el comando `django-admin startproject linkdump`.
   - Aplicación llamada `app` creada dentro del proyecto.

2. **Configuración:**
   - Modificación de `linkdump/settings.py` para incluir la aplicación en `INSTALLED_APPS`.
   - Configuración de la base de datos SQLite.

3. **Modelos y Vistas:**
   - Creación de un modelo `Link` para almacenar URL y descripción.
   - Vistas para manejar la lógica CRUD de los enlaces.
   - Formularios creados en `app/forms.py` para facilitar la entrada de datos.

4. **Rutas y URL:**
   - Configuración de las rutas en `app/urls.py` y `linkdump/urls.py`.

5. **Plantillas HTML:**
   - Plantillas creadas para listar, detallar, crear, editar y borrar enlaces.

6. **Seguridad CSRF:**
   - Implementación de la protección CSRF en formularios.

7. **Poblar la Base de Datos:**
   - Archivo `data.py` creado para insertar datos de ejemplo usando el entorno de Django.

## Requisitos

- Python 3.x
- Django

## Instalación

1. Clona este repositorio.
2. Accede al directorio `linkdump`.
3. Asegúrate de tener un entorno virtual de Python y actívalo.
4. Instala Django: `pip install django`.

## Configuración Inicial

1. Aplica las migraciones para crear las tablas en la base de datos:
   ```bash
   python manage.py migrate
Pobla la base de datos con datos de ejemplo ejecutando:

python data.py
Ejecución del Servidor
Ejecuta el servidor de desarrollo de Django:


python manage.py runserver
Accede a la aplicación en tu navegador en http://localhost:8000.

Funcionalidades
Lista de Enlaces: Ver una lista de todos los enlaces almacenados.
Añadir Nuevo Enlace: Crear un nuevo enlace a través de un formulario.
Editar Enlace: Modificar los detalles de enlaces existentes.
Borrar Enlace: Eliminar enlaces de la base de datos.
Seguridad
El proyecto implementa medidas de seguridad CSRF para proteger los formularios de posibles ataques.

Contribución
Para contribuir, por favor sigue los mejores estándares de codificación y asegúrate de probar antes de enviar cualquier solicitud de extracción.

Licencia
Este proyecto es de código abierto y se distribuye bajo la licencia MIT.

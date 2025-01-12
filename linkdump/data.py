import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linkdump.settings')
django.setup()

from app.models import Link

# Datos de ejemplo para poblar las tablas
links_data = [
    {"url": "https://www.djangoproject.com/", "description": "El sitio oficial de Django"},
    {"url": "https://docs.djangoproject.com/en/stable/", "description": "Documentación oficial de Django"},
    {"url": "https://www.djangoproject.com/community/", "description": "Comunidad de Django"},
]

# Poblar la base de datos
for link in links_data:
    Link.objects.create(url=link['url'], description=link['description'])

print("Datos insertados exitosamente")
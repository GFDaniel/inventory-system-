#!/bin/bash

echo "🔍 Diagnóstico de Migraciones Django"
echo "===================================="

# Verificar entorno virtual
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️ Activando entorno virtual..."
    source inventory-system/bin/activate
fi

echo ""
echo "📋 1. Verificando estructura del proyecto..."
echo "Apps instaladas en settings.py:"
python -c "
import os, sys
sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_backend.settings')
import django
django.setup()
from django.conf import settings
for app in settings.INSTALLED_APPS:
    if 'inventory' in app or 'django' not in app:
        print(f'  ✓ {app}')
"

echo ""
echo "📋 2. Verificando modelos..."
python -c "
import os, sys
sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_backend.settings')
import django
django.setup()
from inventory.models import Product, InventoryMovement
print('  ✓ Product model found')
print('  ✓ InventoryMovement model found')
"

echo ""
echo "📋 3. Estado actual de migraciones..."
python manage.py showmigrations

echo ""
echo "📋 4. Verificando archivos de migración..."
ls -la inventory/migrations/

echo ""
echo "📋 5. Creando migraciones específicas para inventory..."
python manage.py makemigrations inventory --verbosity=2

echo ""
echo "📋 6. Aplicando migraciones..."
python manage.py migrate --verbosity=2

echo ""
echo "📋 7. Verificando tablas creadas..."
python -c "
import os, sys
sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_backend.settings')
import django
django.setup()
from django.db import connection
cursor = connection.cursor()
cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'inventory_%';\")
tables = cursor.fetchall()
print('Tablas de inventory encontradas:')
for table in tables:
    print(f'  ✓ {table[0]}')
"

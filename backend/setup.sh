#!/bin/bash

echo "🚀 Configuración completa del Backend Django"
echo "============================================="

# Verificar que estamos en el directorio correcto
if [ ! -f "manage.py" ]; then
    echo "❌ Error: No se encuentra manage.py. Asegúrate de estar en el directorio backend/"
    exit 1
fi

# Verificar que el entorno virtual está activo
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Advertencia: No hay entorno virtual activo"
    echo "Activando entorno virtual..."
    
    if [ -d "inventory-system" ]; then
        source inventory-system/bin/activate
        echo "✅ Entorno virtual activado"
    else
        echo "❌ No se encuentra el entorno virtual. Ejecuta primero install.sh"
        exit 1
    fi
fi

echo "📋 Verificando instalación de Django..."
python -c "import django; print(f'✅ Django {django.get_version()}')" || {
    echo "❌ Django no está instalado correctamente"
    exit 1
}

echo ""
echo "🗄️  Paso 1: Creando migraciones..."
python manage.py makemigrations

echo ""
echo "🗄️  Paso 2: Aplicando migraciones..."
python manage.py migrate

echo ""
echo "👥 Paso 3: Creando usuarios y datos de prueba..."
python scripts/init_db.py

echo ""
echo "🔍 Paso 4: Verificando configuración..."
python manage.py check

echo ""
echo "✅ ¡Configuración completada exitosamente!"
echo ""
echo "Para iniciar el servidor ejecuta:"
echo "python manage.py runserver"
echo ""
echo "Credenciales disponibles:"
echo "- Admin: admin / admin123"
echo "- Usuario: testuser / test123"
echo ""
echo "URLs importantes:"
echo "- API: http://localhost:8000/api/"
echo "- Admin: http://localhost:8000/admin/"

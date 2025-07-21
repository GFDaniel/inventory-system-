@echo off
echo 🚀 Configuración completa del Backend Django
echo =============================================

REM Verificar que estamos en el directorio correcto
if not exist "manage.py" (
    echo ❌ Error: No se encuentra manage.py. Asegúrate de estar en el directorio backend/
    pause
    exit /b 1
)

REM Activar entorno virtual si existe
if exist "inventory-system\Scripts\activate.bat" (
    echo 🔄 Activando entorno virtual...
    call inventory-system\Scripts\activate.bat
)

echo 📋 Verificando instalación de Django...
python -c "import django; print(f'✅ Django {django.get_version()}')" || (
    echo ❌ Django no está instalado correctamente
    pause
    exit /b 1
)

echo.
echo 🗄️ Paso 1: Creando migraciones...
python manage.py makemigrations

echo.
echo 🗄️ Paso 2: Aplicando migraciones...
python manage.py migrate

echo.
echo 👥 Paso 3: Creando usuarios y datos de prueba...
python scripts\init_db.py

echo.
echo 🔍 Paso 4: Verificando configuración...
python manage.py check

echo.
echo ✅ ¡Configuración completada exitosamente!
echo.
echo Para iniciar el servidor ejecuta:
echo python manage.py runserver
echo.
echo Credenciales disponibles:
echo - Admin: admin / admin123
echo - Usuario: testuser / test123
echo.
echo URLs importantes:
echo - API: http://localhost:8000/api/
echo - Admin: http://localhost:8000/admin/
echo.
pause

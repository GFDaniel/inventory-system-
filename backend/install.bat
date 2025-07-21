@echo off
echo 🔧 Configurando Backend Django...

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no encontrado. Por favor instala Python 3.12+
    pause
    exit /b 1
)

echo ✅ Python encontrado
python --version

REM Crear entorno virtual
echo 📦 Creando entorno virtual...
python -m venv inventory-system

REM Activar entorno virtual
echo 🔄 Activando entorno virtual...
call inventory-system\Scripts\activate

REM Actualizar pip y setuptools
echo ⬆️ Actualizando pip y setuptools...
python -m pip install --upgrade pip setuptools wheel

REM Instalar dependencias
echo 📥 Instalando dependencias...
pip install -r requirements.txt

REM Verificar instalación
echo 🔍 Verificando instalación...
python -c "import django; print(f'Django {django.get_version()} instalado correctamente')"
python -c "import rest_framework; print('Django REST Framework instalado correctamente')"
python -c "import rest_framework_simplejwt; print('JWT instalado correctamente')"

echo ✅ Backend configurado correctamente
pause

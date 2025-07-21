#!/bin/bash

echo "🔧 Configurando Backend Django..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no encontrado. Instalando..."
    # En macOS con Homebrew
    if command -v brew &> /dev/null; then
        brew install python@3.12
    else
        echo "Por favor instala Python 3.12+ manualmente"
        exit 1
    fi
fi

echo "✅ Python encontrado: $(python3 --version)"

# Crear entorno virtual
echo "📦 Creando entorno virtual..."
python3 -m venv inventory-system

# Activar entorno virtual
echo "🔄 Activando entorno virtual..."
source inventory-system/bin/activate

# Actualizar pip y setuptools
echo "⬆️ Actualizando pip y setuptools..."
python -m pip install --upgrade pip setuptools wheel

# Instalar dependencias
echo "📥 Instalando dependencias..."
pip install -r requirements.txt

# Verificar instalación
echo "🔍 Verificando instalación..."
python -c "import django; print(f'Django {django.get_version()} instalado correctamente')"
python -c "import rest_framework; print('Django REST Framework instalado correctamente')"
python -c "import rest_framework_simplejwt; print('JWT instalado correctamente')"

echo "✅ Backend configurado correctamente"

#!/bin/bash

echo "🎨 Configurando Frontend Angular + Ionic"
echo "========================================"

# Verificar Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js no encontrado. Por favor instálalo primero."
    exit 1
fi

echo "✅ Node.js encontrado: $(node --version)"
echo "✅ npm encontrado: $(npm --version)"

# Verificar que estamos en el directorio correcto
if [ ! -f "package.json" ]; then
    echo "❌ Error: No se encuentra package.json. Asegúrate de estar en el directorio frontend/"
    exit 1
fi

echo ""
echo "📦 Instalando dependencias..."
npm install

echo ""
echo "🔧 Verificando instalación de Ionic CLI..."
if ! command -v ionic &> /dev/null; then
    echo "📥 Instalando Ionic CLI globalmente..."
    npm install -g @ionic/cli
else
    echo "✅ Ionic CLI ya está instalado: $(ionic --version)"
fi

echo ""
echo "🔍 Verificando configuración..."
if [ -f "src/app/app.module.ts" ]; then
    echo "✅ Estructura de Angular encontrada"
fi

if [ -f "ionic.config.json" ]; then
    echo "✅ Configuración de Ionic encontrada"
fi

echo ""
echo "✅ Frontend configurado correctamente!"
echo ""
echo "Para iniciar el frontend ejecuta:"
echo "ionic serve"
echo ""
echo "La aplicación estará disponible en:"
echo "http://localhost:8100"

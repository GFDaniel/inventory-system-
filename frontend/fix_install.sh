#!/bin/bash

echo "🔧 Solucionando problemas de instalación del Frontend"
echo "=================================================="

# Verificar Node.js y npm
echo "📋 Verificando versiones..."
echo "Node.js: $(node --version)"
echo "npm: $(npm --version)"

# Limpiar cache de npm
echo ""
echo "🧹 Limpiando cache de npm..."
npm cache clean --force

# Eliminar node_modules y package-lock.json si existen
echo ""
echo "🗑️ Eliminando instalaciones previas..."
rm -rf node_modules
rm -f package-lock.json

# Actualizar npm a la última versión
echo ""
echo "⬆️ Actualizando npm..."
npm install -g npm@latest

# Instalar dependencias con configuración específica
echo ""
echo "📦 Instalando dependencias..."
npm install --legacy-peer-deps

# Verificar instalación
echo ""
echo "🔍 Verificando instalación..."
if [ -d "node_modules" ]; then
    echo "✅ node_modules creado correctamente"
    
    # Verificar paquetes clave
    if [ -d "node_modules/@ionic/angular" ]; then
        echo "✅ Ionic Angular instalado"
    fi
    
    if [ -d "node_modules/@angular/core" ]; then
        echo "✅ Angular Core instalado"
    fi
    
    echo ""
    echo "🎉 Instalación completada!"
    echo ""
    echo "Para iniciar el frontend ejecuta:"
    echo "ionic serve"
    
else
    echo "❌ Error en la instalación"
    echo ""
    echo "Intenta instalar manualmente:"
    echo "npm install @ionic/angular @angular/core @angular/common --legacy-peer-deps"
fi

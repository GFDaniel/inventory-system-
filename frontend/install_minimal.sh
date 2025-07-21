#!/bin/bash

echo "📦 Instalación Mínima del Frontend"
echo "================================="

# Limpiar todo
rm -rf node_modules package-lock.json

# Crear package.json mínimo
cat > package.json << 'EOF'
{
  "name": "inventory-frontend",
  "version": "0.0.1",
  "scripts": {
    "start": "ionic serve",
    "build": "ng build",
    "serve": "ionic serve"
  },
  "dependencies": {
    "@angular/animations": "^16.0.0",
    "@angular/common": "^16.0.0",
    "@angular/compiler": "^16.0.0",
    "@angular/core": "^16.0.0",
    "@angular/forms": "^16.0.0",
    "@angular/platform-browser": "^16.0.0",
    "@angular/platform-browser-dynamic": "^16.0.0",
    "@angular/router": "^16.0.0",
    "@ionic/angular": "^7.0.0",
    "ionicons": "^7.0.0",
    "rxjs": "~7.8.0",
    "tslib": "^2.3.0",
    "zone.js": "~0.13.0"
  },
  "devDependencies": {
    "@angular-devkit/build-angular": "^16.0.0",
    "@angular/cli": "^16.0.0",
    "@angular/compiler-cli": "^16.0.0",
    "@ionic/angular-toolkit": "^9.0.0",
    "typescript": "~5.0.2"
  }
}
EOF

echo "✅ package.json mínimo creado"

# Instalar dependencias básicas
echo ""
echo "📥 Instalando dependencias básicas..."
npm install --legacy-peer-deps

echo ""
echo "🔧 Instalando Ionic CLI si no está disponible..."
if ! command -v ionic &> /dev/null; then
    npm install -g @ionic/cli
fi

echo ""
echo "✅ Instalación mínima completada!"

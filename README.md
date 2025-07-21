# Sistema de Inventario

Sistema completo de gestión de inventario desarrollado con Django (backend) y Angular + Ionic (frontend).

## Tecnologías Utilizadas

### Backend

- **Python** 3.9 o superior
- **Django** 4.2.7
- **Django REST Framework** 3.14.0
- **SQLite** como base de datos
- **JWT** para autenticación

### Frontend

- **Angular** 16.0.0
- **Ionic** 7.0.0
- **TypeScript** 5.0.2
- **RxJS** 7.8.0

## Funcionalidades

### Autenticación

- Inicio de sesión con usuario y contraseña
- Autenticación mediante JWT
- Protección de rutas

### Gestión de Productos

- Crear, editar, eliminar y listar productos
- Campos: nombre, descripción, precio y stock
- Validaciones en los formularios

### Movimientos de Inventario

- Registrar movimientos de entrada (aumenta el stock)
- Registrar movimientos de salida (reduce el stock)
- Validación: las salidas no pueden superar el stock disponible
- Actualización automática del stock
- Historial de movimientos con usuario y fecha

## Instalación y Ejecución

### Prerrequisitos

- Python 3.9 o superior
- Node.js 16 o superior
- npm o yarn

### Backend (Django)

1. **Crear entorno virtual:**

```bash
cd backend
python -m venv inventory-system-venv
source inventory-system-venv/bin/activate  # En Windows: inventory-system-venv\Scripts\activate
```

2. **Instalar dependencias:**

```bash
pip install -r requirements.txt
```

3. **Configurar base de datos:**

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Crear datos de prueba:**

```bash
python scripts/init_db.py
```

5. **Ejecutar servidor:**

```bash
python manage.py runserver
```

El backend estará disponible en: `http://localhost:8000`

### Frontend (Angular + Ionic)

1. **Instalar dependencias:**

```bash
cd frontend
npm install
```

2. **Instalar Ionic CLI (si no está instalado):**

```bash
npm install -g @ionic/cli
```

3. **Ejecutar aplicación:**

```bash
ionic serve
```

La aplicación estará disponible en: `http://localhost:8100`

## Credenciales de Prueba

### Usuario Administrador

- **Usuario:** `admin`
- **Contraseña:** `admin123`

### Usuario de Prueba

- **Usuario:** `testuser`
- **Contraseña:** `test123`

## API Endpoints

### Autenticación

- `POST /api/auth/login/` – Iniciar sesión
- `POST /api/auth/refresh/` – Renovar token
- `GET /api/auth/profile/` – Obtener perfil del usuario

### Productos

- `GET /api/products/` – Listar productos
- `POST /api/products/` – Crear producto
- `GET /api/products/{id}/` – Obtener producto
- `PUT /api/products/{id}/` – Actualizar producto
- `DELETE /api/products/{id}/` – Eliminar producto

### Movimientos

- `GET /api/movements/` – Listar movimientos
- `POST /api/movements/` – Crear movimiento
- `GET /api/movements/?product_id={id}` – Movimientos por producto

## Estructura del Proyecto

```
inventory-system/
├── backend/
│   ├── inventory_backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inventory/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── scripts/
│   │   └── init_db.py
│   ├── requirements.txt
│   └── manage.py
└── frontend/
    ├── src/
    │   ├── app/
    │   │   ├── models/
    │   │   ├── services/
    │   │   ├── guards/
    │   │   ├── interceptors/
    │   │   └── pages/
    │   ├── environments/
    │   └── theme/
    ├── package.json
    └── ionic.config.json
```

## Características Técnicas

### Backend

- Arquitectura RESTful
- Autenticación JWT con tokens de renovación
- Validaciones de negocio (stock no negativo)
- Configuración de CORS para desarrollo
- Panel de administración de Django disponible

### Frontend

- Aplicación híbrida (web/móvil)
- Diseño responsivo con Ionic
- Interceptor HTTP para autenticación automática
- Guards para proteger rutas
- Formularios reactivos con validaciones
- Manejo de estados de carga y errores

## Desarrollo

### Comandos Útiles

**Backend:**

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Acceder al shell de Django
python manage.py shell
```

**Frontend:**

```bash
# Servir en modo desarrollo
ionic serve

# Construir para producción
ionic build

# Ejecutar en dispositivo móvil
ionic capacitor run android
ionic capacitor run ios
```

## Notas Adicionales

- La aplicación está configurada para desarrollo local
- Se utiliza SQLite como base de datos por simplicidad
- Los tokens JWT tienen una duración de 60 minutos
- El frontend se conecta automáticamente al backend en `localhost:8000`
- Todos los endpoints requieren autenticación, excepto el de inicio de sesión

#!/usr/bin/env python
"""
Script para diagnosticar y reparar problemas de base de datos
"""
import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_backend.settings')
django.setup()

from django.core.management import execute_from_command_line
from django.db import connection
from django.contrib.auth.models import User

def check_database():
    """Verificar estado de la base de datos"""
    print("🔍 Verificando estado de la base de datos...")
    
    cursor = connection.cursor()
    
    # Verificar qué tablas existen
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    
    print(f"📋 Tablas encontradas ({len(tables)}):")
    for table in sorted(tables):
        print(f"  ✓ {table}")
    
    # Verificar tablas específicas de inventory
    inventory_tables = [t for t in tables if t.startswith('inventory_')]
    print(f"\n📦 Tablas de inventory ({len(inventory_tables)}):")
    for table in inventory_tables:
        print(f"  ✓ {table}")
    
    return inventory_tables

def reset_migrations():
    """Resetear migraciones de inventory"""
    print("\n🔄 Reseteando migraciones...")
    
    # Eliminar archivos de migración existentes (excepto __init__.py)
    migrations_dir = "inventory/migrations"
    if os.path.exists(migrations_dir):
        for file in os.listdir(migrations_dir):
            if file.endswith('.py') and file != '__init__.py':
                file_path = os.path.join(migrations_dir, file)
                os.remove(file_path)
                print(f"  🗑️ Eliminado: {file}")
    
    # Crear directorio de migraciones si no existe
    os.makedirs(migrations_dir, exist_ok=True)
    
    # Asegurar que __init__.py existe
    init_file = os.path.join(migrations_dir, '__init__.py')
    if not os.path.exists(init_file):
        with open(init_file, 'w') as f:
            f.write('')
        print(f"  ✅ Creado: __init__.py")

def create_fresh_migrations():
    """Crear migraciones desde cero"""
    print("\n📝 Creando migraciones frescas...")
    
    try:
        # Crear migraciones para inventory
        execute_from_command_line(['manage.py', 'makemigrations', 'inventory', '--verbosity=2'])
        print("  ✅ Migraciones creadas para inventory")
        
        # Aplicar migraciones
        execute_from_command_line(['manage.py', 'migrate', '--verbosity=2'])
        print("  ✅ Migraciones aplicadas")
        
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def create_test_data():
    """Crear datos de prueba"""
    print("\n👥 Creando datos de prueba...")
    
    try:
        from inventory.models import Product
        
        # Verificar que las tablas existen
        Product.objects.count()  # Esto fallará si la tabla no existe
        
        # Crear superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            print("  ✅ Superuser 'admin' creado")
        else:
            print("  ℹ️ Superuser 'admin' ya existe")
        
        # Crear usuario de prueba
        if not User.objects.filter(username='testuser').exists():
            User.objects.create_user('testuser', 'test@example.com', 'test123')
            print("  ✅ Usuario 'testuser' creado")
        else:
            print("  ℹ️ Usuario 'testuser' ya existe")
        
        # Crear productos de ejemplo
        products_data = [
            {
                'name': 'Laptop Dell XPS 13',
                'description': 'Laptop ultrabook con procesador Intel i7',
                'price': 25000.00,
                'stock': 10
            },
            {
                'name': 'Mouse Logitech MX Master',
                'description': 'Mouse inalámbrico ergonómico',
                'price': 1500.00,
                'stock': 25
            },
            {
                'name': 'Teclado Mecánico RGB',
                'description': 'Teclado mecánico con iluminación RGB',
                'price': 2500.00,
                'stock': 15
            }
        ]
        
        for product_data in products_data:
            if not Product.objects.filter(name=product_data['name']).exists():
                Product.objects.create(**product_data)
                print(f"  ✅ Producto '{product_data['name']}' creado")
            else:
                print(f"  ℹ️ Producto '{product_data['name']}' ya existe")
        
        return True
    except Exception as e:
        print(f"  ❌ Error creando datos: {e}")
        return False

def main():
    print("🚀 Script de Reparación de Base de Datos")
    print("========================================")
    
    # Paso 1: Verificar estado actual
    inventory_tables = check_database()
    
    # Paso 2: Si no hay tablas de inventory, resetear y recrear
    if not inventory_tables:
        print("\n⚠️ No se encontraron tablas de inventory. Recreando...")
        reset_migrations()
        
        if create_fresh_migrations():
            print("\n✅ Migraciones creadas exitosamente")
            
            # Verificar nuevamente
            inventory_tables = check_database()
            
            if inventory_tables:
                print("\n🎉 ¡Tablas creadas exitosamente!")
                
                # Crear datos de prueba
                if create_test_data():
                    print("\n🎉 ¡Base de datos configurada completamente!")
                    print("\nPuedes ejecutar ahora:")
                    print("python manage.py runserver")
                else:
                    print("\n⚠️ Tablas creadas pero falló la creación de datos")
            else:
                print("\n❌ Las tablas aún no se crearon correctamente")
        else:
            print("\n❌ Falló la creación de migraciones")
    else:
        print("\n✅ Tablas de inventory encontradas. Intentando crear datos...")
        create_test_data()

if __name__ == '__main__':
    main()

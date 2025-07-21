#!/usr/bin/env python
"""
Script para verificar los datos de prueba en la base de datos
"""
import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_backend.settings')
django.setup()

from django.contrib.auth.models import User
from inventory.models import Product, InventoryMovement

def check_users():
    """Verificar usuarios en la base de datos"""
    print("👥 USUARIOS:")
    print("=" * 50)
    
    users = User.objects.all()
    print(f"Total de usuarios: {users.count()}")
    
    for user in users:
        user_type = "Superuser" if user.is_superuser else "Usuario normal"
        print(f"  • {user.username} ({user_type})")
        print(f"    - Email: {user.email}")
        print(f"    - Nombre: {user.first_name} {user.last_name}")
        print(f"    - Activo: {'Sí' if user.is_active else 'No'}")
        print()

def check_products():
    """Verificar productos en la base de datos"""
    print("📦 PRODUCTOS:")
    print("=" * 50)
    
    products = Product.objects.all()
    print(f"Total de productos: {products.count()}")
    
    if products.exists():
        for product in products:
            print(f"  • {product.name}")
            print(f"    - Descripción: {product.description}")
            print(f"    - Precio: ${product.price}")
            print(f"    - Stock: {product.stock}")
            print(f"    - Creado: {product.created_at.strftime('%d/%m/%Y %H:%M')}")
            print()
    else:
        print("  ❌ No hay productos en la base de datos")

def check_movements():
    """Verificar movimientos de inventario"""
    print("📊 MOVIMIENTOS DE INVENTARIO:")
    print("=" * 50)
    
    movements = InventoryMovement.objects.all()
    print(f"Total de movimientos: {movements.count()}")
    
    if movements.exists():
        for movement in movements:
            tipo = "Entrada" if movement.movement_type == "IN" else "Salida"
            print(f"  • {movement.product.name} - {tipo}")
            print(f"    - Cantidad: {movement.quantity}")
            print(f"    - Usuario: {movement.user.username}")
            print(f"    - Descripción: {movement.description}")
            print(f"    - Fecha: {movement.created_at.strftime('%d/%m/%Y %H:%M')}")
            print()
    else:
        print("  ❌ No hay movimientos en la base de datos")

def check_database_tables():
    """Verificar que las tablas existen"""
    print("🗄️ TABLAS DE BASE DE DATOS:")
    print("=" * 50)
    
    from django.db import connection
    cursor = connection.cursor()
    
    # Obtener todas las tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    all_tables = [table[0] for table in cursor.fetchall()]
    
    # Filtrar tablas de inventory
    inventory_tables = [t for t in all_tables if t.startswith('inventory_')]
    auth_tables = [t for t in all_tables if t.startswith('auth_')]
    
    print(f"Total de tablas: {len(all_tables)}")
    print(f"Tablas de autenticación: {len(auth_tables)}")
    print(f"Tablas de inventory: {len(inventory_tables)}")
    
    print("\nTablas de inventory encontradas:")
    for table in inventory_tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"  ✅ {table} ({count} registros)")

def main():
    print("🔍 VERIFICACIÓN DE DATOS DE PRUEBA")
    print("=" * 60)
    print()
    
    try:
        # Verificar tablas
        check_database_tables()
        print()
        
        # Verificar usuarios
        check_users()
        
        # Verificar productos
        check_products()
        
        # Verificar movimientos
        check_movements()
        
        print("✅ RESUMEN:")
        print("=" * 50)
        users_count = User.objects.count()
        products_count = Product.objects.count()
        movements_count = InventoryMovement.objects.count()
        
        print(f"👥 Usuarios: {users_count}")
        print(f"📦 Productos: {products_count}")
        print(f"📊 Movimientos: {movements_count}")
        
        if users_count >= 2 and products_count >= 3:
            print("\n🎉 ¡Los datos de prueba están correctamente creados!")
        else:
            print("\n⚠️ Faltan algunos datos de prueba. Ejecuta: python scripts/init_db.py")
            
    except Exception as e:
        print(f"❌ Error al verificar datos: {e}")
        print("\nPosibles soluciones:")
        print("1. Ejecutar migraciones: python manage.py migrate")
        print("2. Crear datos de prueba: python scripts/init_db.py")

if __name__ == '__main__':
    main()

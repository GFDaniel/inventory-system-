import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_backend.settings')
django.setup()

from django.contrib.auth.models import User
from django.core.management import execute_from_command_line
from inventory.models import Product, InventoryMovement

def run_migrations():
    """Ejecutar migraciones antes de crear datos"""
    print("Running migrations...")
    try:
        execute_from_command_line(['manage.py', 'makemigrations'])
        execute_from_command_line(['manage.py', 'migrate'])
        print("Migrations completed successfully!")
    except Exception as e:
        print(f"Error running migrations: {e}")
        return False
    return True

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser 'admin' created with password 'admin123'")
    else:
        print("Superuser 'admin' already exists")

def create_test_user():
    if not User.objects.filter(username='testuser').exists():
        User.objects.create_user('testuser', 'test@example.com', 'test123')
        print("Test user 'testuser' created with password 'test123'")
    else:
        print("Test user 'testuser' already exists")

def create_sample_products():
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
        },
        {
            'name': 'Monitor 4K 27"',
            'description': 'Monitor 4K de 27 pulgadas',
            'price': 8000.00,
            'stock': 8
        },
        {
            'name': 'Auriculares Sony WH-1000XM4',
            'description': 'Auriculares inalámbricos con cancelación de ruido',
            'price': 6000.00,
            'stock': 12
        }
    ]
    
    for product_data in products_data:
        if not Product.objects.filter(name=product_data['name']).exists():
            Product.objects.create(**product_data)
            print(f"Product '{product_data['name']}' created")
        else:
            print(f"Product '{product_data['name']}' already exists")

if __name__ == '__main__':
    print("Initializing database...")
    
    # Primero ejecutar migraciones
    if not run_migrations():
        print("Failed to run migrations. Exiting...")
        sys.exit(1)
    
    # Luego crear usuarios y productos
    create_superuser()
    create_test_user()
    create_sample_products()
    print("Database initialization completed!")

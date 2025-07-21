from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

class InventoryMovement(models.Model):
    MOVEMENT_TYPES = [
        ('IN', 'Entrada'),
        ('OUT', 'Salida'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='movements')
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPES)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.movement_type} - {self.quantity}"

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Validar que no se pueda hacer una salida mayor al stock disponible
        if self.movement_type == 'OUT' and self.quantity > self.product.stock:
            raise ValueError("No se puede realizar una salida mayor al stock disponible")
        
        # Guardar el movimiento
        super().save(*args, **kwargs)
        
        # Actualizar el stock del producto
        if self.movement_type == 'IN':
            self.product.stock += self.quantity
        else:  # OUT
            self.product.stock -= self.quantity
        
        self.product.save()

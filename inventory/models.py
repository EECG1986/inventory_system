from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)  # Asegúrate de que este campo exista
    email = models.EmailField()  # Asegúrate de que este campo exista
    phone = models.CharField(max_length=15)  # Asegúrate de que este campo exista

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Modelo que representa a un producto.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

def __str__(self):
    """
    Devuelve una representación en cadena del modelo.
    """
    return self.name


class Order(models.Model):
    """
    Modelo que representa un pedido.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    """
    Devuelve una representación en cadena del modelo.
    """
    return f"{self.product.name} - {self.quantity}"
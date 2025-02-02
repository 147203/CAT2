from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)  # Name of the customer
    email = models.EmailField(unique=True)  # Unique email for each customer

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE, 
        related_name='orders'
    )  # Establishes a one-to-many relationship
    order_date = models.DateTimeField(auto_now_add=True)  # Date when the order was placed
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total order cost

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"


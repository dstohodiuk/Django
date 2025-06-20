from django.db import models


class GPUBrand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField(default=2000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class GPU(models.Model):
    MEMORY_CHOICES = [
        ('GDDR5', 'GDDR5'),
        ('GDDR6', 'GDDR6'),
        ('GDDR6X', 'GDDR6X'),
    ]

    brand = models.ForeignKey(
        GPUBrand, on_delete=models.SET_NULL, null=True, blank=True)
    model = models.CharField(max_length=100)
    memory_gb = models.PositiveIntegerField(default=8)
    core_clock_mhz = models.PositiveIntegerField()
    boost_clock_mhz = models.PositiveIntegerField(null=True, blank=True)
    memory_type = models.CharField(
        max_length=10, choices=MEMORY_CHOICES, default='GDDR6')
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='gpu_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.brand.name} {self.model}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(
        GPUBrand, on_delete=models.CASCADE, related_name='gpus')

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Замовлення {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    gpu = models.ForeignKey('GPU', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

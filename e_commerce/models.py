from django.db import models

# Create your models here.

brand_choices=(
    ('Apple','Apple'),
    ('Samsung', 'Samsung'),
    ('Motorola', 'Motorola'),
    ('Vivo', 'Vivo'),
    ('Oppo','Oppo'),
    ('Xiaomi', 'Xiaomi'),
    ('Oneplus', 'Oneplus')
)

storage_choices=(
    ('32','32'),
    ('64','64'),
    ('128','128'),
    ('256','256'),
    ('512','512')
)

class Product(models.Model):
    brand = models.CharField(max_length=100, default= 0, choices= brand_choices)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    storage = models.CharField(max_length=4, choices= storage_choices, default=0)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics', default= 0)
    img_1 = models.ImageField(upload_to='pics', default= 0)
    img_2 = models.ImageField(upload_to='pics', default= 0)
    img_3 = models.ImageField(upload_to='pics', default= 0)
from django.db import models

# Create your models here.

LANGUAGE_TYPE= [
    ('AR', 'Arabic'),
    ('CHI', 'Chinese'),
    ('ENG', 'English'),
    ('FRA', 'French'),
    ('GER', 'German'),
    ('HIN', 'Hindi'),
    ('JPN', 'Japanese'),
    ('SPA', 'Spanish'),   
]

CURRENCY_TYPE = [
    ('CNY', 'Chinese Yuan'),
    ('EUR', 'Euro'),
    ('GBP', 'Pound'),
    ('INR', 'Indian Rupee'),
    ('JPY', 'Japanese Yen'),
    ('NGN', 'Nigerian Naira'),
    ('USD', 'US Dollar'),
]

# Create your models here.

class Provider(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=30, null=False, blank=False, unique=True)
    phone_number = models.BigIntegerField(null=False, blank=False, unique=True)
    language = models.CharField(max_length =3, choices = LANGUAGE_TYPE)
    currency = models.CharField(max_length=3, choices = CURRENCY_TYPE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering =['id']
        
class ServiceArea(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits = 6 , decimal_places = 2, default = 0.00 )
    poly =  models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']
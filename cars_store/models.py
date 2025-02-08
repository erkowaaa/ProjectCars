from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    username = models.CharField(max_length=32)
    ROLE_CHOICES = [
        ('Администратор', 'Администратор'),
        ('Продавец', 'Продавец'),
        ('Покупатель', 'Покупатель')
    ]
    phone_number = PhoneNumberField(unique=True)
    role_status = models.CharField(max_length=100, choices=ROLE_CHOICES, default='Администратор')

    def __str__(self):
        return {self.username}


class Car(models.Model):
    brand = models.CharField(max_length=16)
    model = models.CharField(max_length=16)
    year = models.DateField(auto_now=True)
    fuel_type = models.DecimalField(max_digits=2, decimal_places=1)
    transmission = models.CharField(max_length=16)
    image = models.ImageField(upload_to='cars_images/')
    description = models.TextField()
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand


class Auction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_price = models.PositiveSmallIntegerField(default=0)
    min_price = models.PositiveSmallIntegerField(default=0)
    start_time = models.DateField(auto_now=True)
    end_time = models.DateField(auto_now=True)
    STATUS_CHOICES = [
        ('Активен', 'Активен'),
        ('Завершен', 'Завершен'),
        ('Отменен', 'Отменен')
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Активен')

    def __str__(self):
        return self.car


class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.auction


class Feedback(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Auction, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return self.seller





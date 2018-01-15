from django.db import models

# Create your models here.


class TokenData(models.Model):
    price = models.DecimalField(max_digits=32, decimal_places=8)
    percentage_holds = models.DecimalField(max_digits=10, decimal_places=2)
    total_token = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)
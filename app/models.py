from django.db import models

class Cinemas(models.Model):
    """
    Модель для хранения информации о кинотеатрах
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    address_street = models.CharField(max_length=300)
    address_full = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cinemas'
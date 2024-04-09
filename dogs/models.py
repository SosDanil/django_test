from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Breed(models.Model):
    name = models.CharField(max_length=50, verbose_name='порода')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'
        ordering = ('name', )


class Dog(models.Model):
    name = models.CharField(max_length=50, verbose_name='кличка собаки')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='порода')
    photo = models.ImageField(upload_to='dogs/', verbose_name='фото', **NULLABLE)
    birthdate = models.DateField(verbose_name='дата рождения', **NULLABLE)

    def __str__(self):
        return f'{self.name}, порода - {self.breed}'

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'
        ordering = ('name', )



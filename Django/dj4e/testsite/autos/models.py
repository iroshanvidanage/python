from django.db import models
from django.core.validators import MinLengthValidator


class Make(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Enter a vehicle make (e.g. Dodge, Lexus, Mustang)',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )

    def __str__(self):
        """String for representing the Model Object"""
        return self.name


class Auto(models.Model):
    nickname = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Nickname should be greater than 1")]
    )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname


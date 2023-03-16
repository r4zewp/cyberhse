from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=40)
    label = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name


class Player(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    favorite_map = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Participant(models.Model):
    email = models.EmailField()
    telegram = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    applied = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.name


class Partner(models.Model):
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    applied = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.name

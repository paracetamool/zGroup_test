from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

User = get_user_model()

class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название комнаты")
    capacity = models.PositiveIntegerField(verbose_name="Вместимость")
    floor = models.PositiveIntegerField(verbose_name="Этаж")

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Комната")
    date = models.DateField(verbose_name="Дата бронирования")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"

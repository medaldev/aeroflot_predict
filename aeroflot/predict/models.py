from django.db import models


class Name(models.Model):
    """Абстрактная модель "Название" """

    name = models.CharField(max_length=200, verbose_name="Название")

    class Meta:
        abstract = True


class City(Name):
    """Таблица "Город" """

    class Meta:
        verbose_name = "Города"
        verbose_name_plural = verbose_name


class Airplane(Name):
    """Таблица "Самолет" """

    like = models.IntegerField(verbose_name="Тип судна")

    class Meta:
        verbose_name = "Воздушные судна"
        verbose_name_plural = verbose_name


class Airport(Name):
    """Таблица "Аэропорты" """

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="airports",
        verbose_name="Город"
    )

    class Meta:
        verbose_name = "Аэропорт"
        verbose_name_plural = "Аэропорты"


class Flight(models.Model):
    """Таблица "Рейсы" """

    from_city = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="flights_from",
        verbose_name="Город вылета"
    )
    to_city = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="flights_to",
        verbose_name="Город прилета"
    )
    price = models.FloatField(verbose_name="Цена")
    airplane = models.ForeignKey(
        Airplane,
        on_delete=models.CASCADE,
        related_name="flights_airplane",
        verbose_name="Самолет"
    )
    time_depart = models.DateTimeField(verbose_name="Время вылета")
    time_arrive = models.DateTimeField(verbose_name="Время прилета")
    time_left = models.DateField(verbose_name="Время до отправления")
    visible = models.BooleanField()
    available = models.BooleanField()

from django.db import models
from django.db.models import CharField, DateField


class Product(models.Model):
    name_product = CharField(max_length=100, help_text="Укажите название продукта")
    model = CharField(max_length=100, help_text="Укажите модель продукта")
    release_date = DateField(help_text="Дата выхода продукта на рынок")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Network(models.Model):
    name = models.CharField(
        max_length=100, unique=True, help_text="Укажите название поставщика"
    )

    # Контакты
    email = models.EmailField(verbose_name="Email", help_text="Укажите Email")
    country = models.CharField(
        max_length=100, verbose_name="Страна", help_text="Укажите страну"
    )
    city = models.CharField(
        max_length=100, verbose_name="Город", help_text="Укажите город"
    )
    street = models.CharField(
        max_length=100, verbose_name="Улица", help_text="Укажите улицу"
    )
    house_number = models.CharField(
        max_length=100, verbose_name="Номер дома", help_text="Укажите номер дома"
    )

    products = models.ManyToManyField(Product, blank=True)

    supplier = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL
    )

    debt_to_supplier = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность перед поставщиком",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Сеть по продаже"
        verbose_name_plural = "Сети по продаже"

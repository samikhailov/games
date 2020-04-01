from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Колода"
        verbose_name_plural = "Колоды"


class Card(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards', verbose_name='Колода')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"
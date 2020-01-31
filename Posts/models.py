from django.db import models


class GenreModel(models.Model):
    title = models.CharField(max_length=120, verbose_name="Жанр")

    def __str__(self):
        return self.title


class AnimeModel(models.Model):
    classification_choices = [
        (0,  "Для всех"),
        (12, "Для лиц старше 12 лет"),
        (16, "Для лиц старше 16 лет"),
        (18, "Для лиц старше 18 лет")
    ]
    title = models.CharField(max_length=120, verbose_name="Название Аниме")
    title_orig = models.CharField(max_length=120, verbose_name="Оригинальное название Аниме")
    text = models.TextField(verbose_name="Описание")
    date = models.DateField(verbose_name="Дата выпуска")
    genre = models.ManyToManyField(GenreModel, related_name="genre")
    info = models.TextField(verbose_name="Прочая информация")
    image = models.ImageField(verbose_name="Изображение 300x450")
    classification = models.CharField(choices=classification_choices, default=classification_choices[0], max_length=50)

    def __str__(self):
        return self.title
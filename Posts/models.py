from django.db import models


class GenreModel(models.Model):
    title = models.CharField(max_length=240, verbose_name="Жанр")

    def __str__(self):
        return self.title


class AnimeModel(models.Model):
    title = models.CharField(max_length=240, verbose_name="Название аниме")
    description = models.TextField(max_length=10240, verbose_name="Описание", blank=True)
    image = models.URLField(verbose_name="Изображение")
    studio = models.CharField(max_length=240, verbose_name="Студия", blank=True)
    translate = models.CharField(max_length=240, verbose_name="Перевод", blank=True)
    sound = models.CharField(max_length=240, verbose_name="Озвучивание", blank=True)
    author = models.CharField(max_length=240, verbose_name="Автор оригинала/Сценарист", blank=True)
    director = models.CharField(max_length=240, verbose_name="Режиссер", blank=True)
    date = models.CharField(max_length=240, verbose_name="Дата выпуска", blank=True)
    episodes = models.IntegerField(verbose_name="Количество серий", blank=True)
    genre = models.ManyToManyField(GenreModel, related_name="anime", verbose_name="Жанр", blank=True)
    country = models.CharField(max_length=240, verbose_name="Страна", blank=True)
    year = models.IntegerField(verbose_name="Год", blank=True)

    def __str__(self):
        return self.title
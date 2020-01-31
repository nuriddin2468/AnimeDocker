from django.db import models


class GenreModel(models.Model):
    title = models.CharField(max_length=120, verbose_name="Жанр")

    def __str__(self):
        return self.title


class AnimeModel(models.Model):
    title = models.CharField(max_length=240, verbose_name="Название аниме")
    description = models.TextField(max_length=10240, verbose_name="Описание")
    image = models.URLField(verbose_name="Изображение")
    studio = models.CharField(max_length=120, verbose_name="Студия", default=None)
    translate = models.CharField(max_length=120, verbose_name="Перевод", default=None)
    sound = models.CharField(max_length=120, verbose_name="Озвучивание", default=None)
    author = models.CharField(max_length=120, verbose_name="Автор оригинала/Сценарист", default=None)
    director = models.CharField(max_length=120, verbose_name="Режиссер", default=None)
    date = models.CharField(max_length=120, verbose_name="Дата выпуска", default=None)
    episodes = models.IntegerField(verbose_name="Количество серий", default=None)
    genre = models.ManyToManyField(GenreModel, related_name="anime", verbose_name="Жанр", default=None)
    country = models.CharField(max_length=120, verbose_name="Страна", default=None)
    year = models.IntegerField(verbose_name="Год", default=None)

    def __str__(self):
        return self.title
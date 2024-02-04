from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    duration = models.IntegerField(null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


STARS_CHOICES = (
    (i, '* ' * i) for i in range(1, 6)
)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=STARS_CHOICES, null=True)

    def __str__(self):
        return self.movie.title


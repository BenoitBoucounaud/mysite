from django.db import models


class Author(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    SEX_CHOICES = [
        (MALE, 'male'),
        (FEMALE, 'female'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )
    adress = models.CharField(max_length=50)
    region = models.IntegerField()
    country = models.CharField(max_length=20)

class Article(models.Model):
    article = models.TextField()
    title = models.TextField()
    author = models.ForeignKey(
        Author,
        on_delete = models.CASCADE,
    )
    pub_date = models.DateTimeField()

from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    copy_count = models.SmallIntegerField(default=0)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return "{}--{}".format(self.title, self.author)
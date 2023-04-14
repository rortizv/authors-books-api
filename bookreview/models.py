from django.db import models


class Author(models.Model):
    objects = models.Manager()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Author ({ self.first_name}, {self.last_name})'


class Book(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.title
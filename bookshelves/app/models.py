from django.db import models


class Bookshelf(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def get_books(self):
        return self.books.all().order_by('title')


class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    shelf = models.ForeignKey(
        Bookshelf, related_name='books',
        on_delete=models.SET_NULL, null=True)

    def assign_to(self, shelf):
        self.shelf = shelf
        self.save()

    def get_shelf(self):
        return self.shelf

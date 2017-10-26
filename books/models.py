# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import settings


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    cover_url = models.CharField(max_length=200)
    description = models.TextField()


    genre = models.CharField(max_length=200)
    price = models.FloatField()
    publisher = models.CharField(max_length=100)
    release_date = models.DateTimeField('publishing date')

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    rating = models.PositiveIntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'review for {0}: rating {1}'.format(self.book, self.rating)

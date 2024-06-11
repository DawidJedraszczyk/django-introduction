from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)  # Kolumna tekstowa z ograniczoną liczbąznaków
    content = models.TextField()  # Kolumna tekstowa bez ograniczenia długości
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(
        auto_now_add=True)  # Kolumna daty i czasu, automatycznie ustawiana przy tworzeniu
    updated_at = models.DateTimeField(
        auto_now=True)  # Kolumna daty i czasu, automatycznie aktualizowana przy zapisie

    def __str__(self):
        return self.title  # Reprezentacja obiektu jako tekst (nazwa tytułu postu)


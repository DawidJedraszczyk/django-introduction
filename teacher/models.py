from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.TextField()
    age = models.DecimalField(max_digits=5, decimal_places=2)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.title  # Reprezentacja obiektu jako tekst (nazwa tytułu postu)

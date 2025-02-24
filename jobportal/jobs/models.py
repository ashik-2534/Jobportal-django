from django.db import models

# Create your models here.
class Job(models.Model):
    tittle = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tittle

from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cover_letter = models.TextField()
    subbited_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} applied for {self.job.title}"
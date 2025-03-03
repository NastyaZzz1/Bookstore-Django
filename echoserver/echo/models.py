from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    author = models.CharField(max_length=80, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    genre = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        app_label = 'apfelschuss.votes'
        db_table = 'books'
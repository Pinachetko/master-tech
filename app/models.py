from django.db import models

# Create your models here.


class Sections(models.Model):
    class Meta:
        db_table = "Sections"
    name = models.CharField(max_length=200)
    href = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Services(models.Model):
    class Meta:
        db_table = "Services"
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    notes = models.CharField(max_length=500, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return (self.name)

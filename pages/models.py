from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Count', blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, blank=True)
    telephone = models.CharField(max_length=30)
    email = models.EmailField()
    address = None

    def __str__(self):
        return self.first_name + ': ' + self.telephone

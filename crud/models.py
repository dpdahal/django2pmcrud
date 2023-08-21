from django.db import models

# Create your models here.
class Students(models.Model):
    gender_field=(
        ('male','Male'),
        ('female','Female')
    )
    language_field=(
        ('english','English'),
        ('hindi','Hindi'),
        ('nepali','Nepali')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    gender = models.CharField(choices=gender_field,max_length=6)
    language = models.CharField(choices=language_field,max_length=50)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='students/',blank=True,null=True)

    def language_list(self):
        return self.language.split(',')
from django.db import models


class Aktyor(models.Model):
    ism=models.CharField(max_length=120)
    mamlakat=models.CharField(max_length=120)
    jins=models.CharField(max_length=45,choices=[('Erkak','Erkak'),('ayol','ayol')])
    def __str__(self):
        return self.ism
class Kino(models.Model):
    nom=models.CharField(max_length=120)
    yil=models.DateField()
    j=[("fantastika", "fantastika"),("badiy","badiy"),("hujjatli", "hujjatli")]
    janr=models.CharField(max_length=120,choices=j)
    aktyorlar=models.ManyToManyField(Aktyor)
    def __str__(self):
        return f"{self.nom},{self.janr}"
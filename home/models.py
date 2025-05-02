from django.db import models

class Skin(models.Model):
    arma = models.CharField(max_length=20)
    skin_pack = models.CharField(max_length=20)
    fecha_creacion = models.DateField(null=True)

    def __str__(self):
        return f"{self.arma} - {self.skin_pack}"
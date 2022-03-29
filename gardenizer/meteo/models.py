from django.db import models


class MeteoData(models.Model):

    day = models.IntegerField()
    weather = models.IntegerField()
    tmin = models.IntegerField()
    tmax = models.IntegerField()
    probarain = models.IntegerField()
    probafrost = models.IntegerField()
    probawind = models.IntegerField()
    insee = models.CharField(max_length=10)
    datetime = models.DateTimeField()

    class Meta:
        verbose_name = "Meteo"

    def __str__(self):
        return f"{self.insee}"

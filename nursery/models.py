from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=30)
    is_alive = models.BooleanField(default=True)

class Collection(models.Model):
    plants = models.ForeignKey(Plant, on_delete=models.CASCADE)

    @property
    def num_plants(self):
        return len(self.plants.filter(is_alive=True))

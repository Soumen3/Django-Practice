from django.db import models

class RelatedModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    related_model = models.ForeignKey(RelatedModel, on_delete=models.CASCADE, related_name='mymodel_set')

    def __str__(self):
        return self.name

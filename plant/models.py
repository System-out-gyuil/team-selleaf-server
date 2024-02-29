from django.db import models

from selleaf.models import Period


class Plant(Period):
    plant_name = models.CharField(max_length=50,null=False,blank=False)

    class Meta:
        abstract = True
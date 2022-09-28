from django.db import models
from .colleges import *
from .programs import *


class Program(models.Model):

    name = models.CharField(max_length=255, null=False,
                            blank=False, unique=True)
    college = models.CharField(max_length=255, null=False, blank=False,
                               choices=college_choices, default=CIVE)
    description = models.TextField(null=True, blank=True)
    years_of_study = models.SmallIntegerField()
    fee = models.PositiveIntegerField()
    knowledge = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    competences = models.TextField(null=True, blank=True)
    special_requirements = models.TextField(null=True, blank=True)
    fields_of_work = models.TextField()

    def __str__(self):
        return self.name

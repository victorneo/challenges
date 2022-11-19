from django.db import models


class TimeTracked():
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Trial(models.Model, TimeTracked):
    '''A trial consists of a set of stages.'''

    name = models.CharField(max_length=255, null=False, blank=False)
    summary = models.TextField()
    description = models.TextField()
    hidden = models.BooleanField(default=True)


class Stage(models.Model, TimeTracked):
    name = models.CharField(max_length=255, null=False, blank=False)
    summary = models.TextField()
    description = models.TextField()
    hidden = models.BooleanField(default=True)

    trial = models.ForeignKey(Trial, on_delete=models.CASCADE)

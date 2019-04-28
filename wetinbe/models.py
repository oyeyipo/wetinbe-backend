from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides 
    self-updating ``created`` and ``updated`` fields.
    """
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True
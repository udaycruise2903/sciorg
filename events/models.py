import uuid
from django.db import models
from django.urls import reverse

class Event(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    title = models.CharField(max_length=300)
    organiser = models.CharField(max_length=300)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", args=[str(self.id)])

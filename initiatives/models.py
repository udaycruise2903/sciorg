import uuid
from django.db import models
from django.urls import reverse

class Initiative(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    title = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("initiative_detail", args=[str(self.id)])

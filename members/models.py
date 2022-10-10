import uuid
from django.db import models
from django.urls import reverse

class Member(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    name = models.CharField(max_length=300)
    qualification = models.CharField(max_length=50)
    profession = models.CharField(max_length=200)
    designation = models.CharField(max_length=70)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("member_detail", args=[str(self.id)])

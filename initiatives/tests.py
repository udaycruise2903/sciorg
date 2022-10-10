from django.test import  TestCase
from django.urls import reverse

from .models import Initiative


class InitiativeTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.initiative = initiative.objects.create(
            title="sky watch month",
            description ="November of every year is celebrated as skywatch month",
        )

    def test_initiative_listing(self):
        self.assertEqual(f"{self.initiative.title}", "sky watch event")
        self.assertEqual(f"{self.initiative.description}", "November of every year is celebrated as sky watch of month")

    def test_initiative_list_view(self):
        response = self.client.get(reverse("initiative_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "sky watch month")
        self.assertTemplateUsed(response, "initiatives/initiative_list.html")

    def test_initiative_detail_view(self):
        response = self.client.get(self.initiative.get_absolute_url())
        no_response = self.client.get("/initiative/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "sky watch month")
        self.assertTemplateUsed(response, "initiatives/initiative_detail.html")

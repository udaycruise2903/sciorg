from django.test import  TestCase
from django.urls import reverse

from .models import Event


class EventTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.event = Event.objects.create(
            title="Intro to git",
            organiser = "foss club",
            start_date = "2022-10-09",
            end_date = "2022-10-10",
            start_time = "12:00:00",
            end_time = "16:00:00",
            description ="Git is a VCS tool",
        )

    def test_event_listing(self):
        self.assertEqual(f"{self.event.title}", "Intro to git")
        self.assertEqual(f"{self.event.organiser}", "foss club")
        self.assertEqual(f"{self.event.start_date}", "2022-10-09")
        self.assertEqual(f"{self.event.end_date}", "2022-10-10")
        self.assertEqual(f"{self.event.start_time}", "12:00:00")
        self.assertEqual(f"{self.event.end_time}", "16:00:00")
        self.assertEqual(f"{self.event.description}", "Git is a VCS tool")

    def test_event_list_view(self):
        response = self.client.get(reverse("event_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Intro to git")
        self.assertTemplateUsed(response, "events/event_list.html")

    def test_event_detail_view(self):
        response = self.client.get(self.event.get_absolute_url())
        no_response = self.client.get("/events/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Intro to git")
        self.assertTemplateUsed(response, "events/event_detail.html")

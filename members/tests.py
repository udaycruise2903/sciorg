from django.test import  TestCase
from django.urls import reverse

from .models import Member


class MemberTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.member = Member.objects.create(
            name="Mr. John Doe",
            qualification = "M.Sc Physics",
            profession = "Asst. Professor",
            designation = "Member",
            description ="Mr. JD is a member of the club",
        )

    def test_member_listing(self):
        self.assertEqual(f"{self.member.name}", "Mr. John Doe")
        self.assertEqual(f"{self.member.qualification}", "M.Sc Physics")
        self.assertEqual(f"{self.member.profession}", "Asst. Professor")
        self.assertEqual(f"{self.member.designation}", "Member")
        self.assertEqual(f"{self.member.description}", "Mr. JD is a member of the club")

    def test_member_list_view(self):
        response = self.client.get(reverse("member_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mr. John Doe")
        self.assertTemplateUsed(response, "members/member_list.html")

    def test_member_detail_view(self):
        response = self.client.get(self.member.get_absolute_url())
        no_response = self.client.get("/members/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Mr. John Doe")
        self.assertTemplateUsed(response, "members/member_detail.html")

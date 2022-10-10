from django.views.generic import ListView, DetailView

from .models import Member


class MemberListView(ListView):
    model = Member
    context_object_name = "member_list"
    template_name = "members/member_list.html"


class MemberDetailView(DetailView):
    model = Member
    context_object_name = "member"
    template_name = "members/member_detail.html"



from django.views.generic import ListView, DetailView

from members.models import Member
from .models import Event, Member


class EventListView(ListView):
    model = Event
    context_object_name = "event_list"
    template_name = "events/event_list.html"


class EventDetailView(DetailView):
    model = Event
    context_object_name = "event"
    template_name = "events/event_detail.html"




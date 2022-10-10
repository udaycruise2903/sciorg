from django.views.generic import ListView, DetailView

from .models import Initiative


class InitiativeListView(ListView):
    model = Initiative
    context_object_name = "initiative_list"
    template_name = "initiatives/initiative_list.html"


class InitiativeDetailView(DetailView):
    model = Initiative
    context_object_name = "initiative"
    template_name = "initiatives/initiative_detail.html"



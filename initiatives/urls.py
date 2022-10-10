from django.urls import path

from .views import InitiativeListView, InitiativeDetailView

urlpatterns = [
    path('', InitiativeListView.as_view(), name="initiative_list"),
    path('<uuid:pk>', InitiativeDetailView.as_view(), name="initiative_detail"),
]

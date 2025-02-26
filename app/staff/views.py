from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Staff


class StaffListView(ListView):
    model = Staff


class StaffDetailView(DetailView):
    model = Staff


class StaffCreateview(CreateView):
    model = Staff
    fields = "__all__"


class StaffUpdateView(UpdateView):
    model = Staff
    template_name = "staff/staff_form.html"
    fields = "__all__"
    success_url = reverse_lazy("staff-list")

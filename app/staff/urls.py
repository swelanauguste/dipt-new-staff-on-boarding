from django.urls import path

from . import views

urlpatterns = [
    path("", views.StaffCreateview.as_view(), name="staff-create"),
    path("staff/", views.StaffListView.as_view(), name="staff-list"),
    path("detail/<int:pk>/", views.StaffDetailView.as_view(), name="staff-detail"),
    path("update/<int:pk>/", views.StaffUpdateView.as_view(), name="staff-update"),
]
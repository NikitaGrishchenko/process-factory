from django.urls import path

from .views import ReleaseDetailView, ReleaseListView

app_name = "release"

urlpatterns = [
    path("", ReleaseListView.as_view(), name="list"),
    path("<int:pk>/", ReleaseDetailView.as_view(), name="detail"),
]

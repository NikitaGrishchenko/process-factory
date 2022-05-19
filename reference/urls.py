from django.urls import path

from .views import QualityLibraryListView, SiteListView, UsefulMaterialsView

app_name = "reference"

urlpatterns = [
    path("sites/", SiteListView.as_view(), name="sites"),
    path("quality-library/", QualityLibraryListView.as_view(), name="quality-library"),
    path("useful-materials/", UsefulMaterialsView.as_view(), name="useful-materials"),
]

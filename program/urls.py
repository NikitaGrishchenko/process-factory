from django.urls import path

from .views import EducationalProgramDetailView, registration_to_program

app_name = 'program'

urlpatterns = [
    path('detail/<int:pk>/', EducationalProgramDetailView.as_view(), name='detail'),
    path("registration/<int:pk>/", registration_to_program, name="registration"),
]

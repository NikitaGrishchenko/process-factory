from django.urls import path

from .views import (EducationalProgramDetailView, EducationalProgramListView,
                    registration_to_program, send_feedback)

app_name = 'program'

urlpatterns = [
    path('', EducationalProgramListView.as_view(), name='list'),
    path('detail/<int:pk>/', EducationalProgramDetailView.as_view(), name='detail'),
    path("registration/<int:pk>/", registration_to_program, name="registration"),
    path("send-feedback/<int:pk>/", send_feedback, name="send-feedback"),
]

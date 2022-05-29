from django.urls import path

from .views import BusinessGamesDetailView, registration_to_program, send_feedback

app_name = 'business'

urlpatterns = [
    path('detail/<int:pk>/', BusinessGamesDetailView.as_view(), name='detail'),
    path("registration/<int:pk>/", registration_to_program, name="registration"),
    path("send-feedback/<int:pk>/", send_feedback, name="send-feedback"),
]

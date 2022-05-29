from django.urls import path

from .views import (BusinessGamesDetailView, BusinessGamesListView,
                    registration_to_program, send_feedback)

app_name = 'business'

urlpatterns = [
    path('', BusinessGamesListView.as_view(), name='list'),
    path('detail/<int:pk>/', BusinessGamesDetailView.as_view(), name='detail'),
    path("registration/<int:pk>/", registration_to_program, name="registration"),
    path("send-feedback/<int:pk>/", send_feedback, name="send-feedback"),
]

from django.urls import path

from .views import (AccountVeiw, EmployeeDetailView, ErrorView,
                    QuestionsFromGuestsForm, RegistrationView, SuccessView,
                    ThanksView)

app_name = 'user'

urlpatterns = [
    path('account/', AccountVeiw.as_view(), name='account'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('feedback/', QuestionsFromGuestsForm.as_view(), name='feedback'),
    path('employee-detail/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path("thanks/", ThanksView.as_view(), name="thanks"),
    path("success/", SuccessView.as_view(), name="success"),
    path("error/", ErrorView.as_view(), name="error"),
]

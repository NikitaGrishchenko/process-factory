from django.urls import path

from .views import (EmployeeDetailView, ErrorView, RegistrationView,
                    SuccessView, ThanksView)

app_name = 'user'

urlpatterns = [
    # path('account/', AccountVeiw.as_view(), name='account'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('employee-detail/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path("thanks/", ThanksView.as_view(), name="thanks"),
    path("success/", SuccessView.as_view(), name="success"),
    path("error/", ErrorView.as_view(), name="error"),
]

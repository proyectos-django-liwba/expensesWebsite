from django.urls import path
from .views import RegisterView, LoginView, ResetPasswordView, ForgotPasswordView


urlpatterns = [
   path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
]

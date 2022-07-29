from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views.profile import UserProfileView
from accounts.views.register import RegisterView

app_name = 'accounts'

urlpatterns = [
    path('account/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('accounts/logout/', LogoutView.as_view(), name="logout"),
    path('registration/', RegisterView.as_view(), name="registration"),
]

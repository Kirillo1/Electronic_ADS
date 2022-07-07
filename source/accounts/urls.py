from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import UserProfileView

app_name = 'accounts'

urlpatterns = [
    path('account/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]

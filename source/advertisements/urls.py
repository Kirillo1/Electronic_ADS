from django.urls import path

from advertisements.views.advertisements import IndexView

app_name = "advertisements"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]

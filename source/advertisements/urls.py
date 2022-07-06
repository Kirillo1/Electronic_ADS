from django.urls import path

from advertisements.views.advertisements import IndexView, AdvertisementDetailView, AdvertisementCreateView

app_name = "advertisements"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('advertisement/<int:pk>/', AdvertisementDetailView.as_view(), name="advertisement_detail_view"),
    path('advertisement/add/', AdvertisementCreateView.as_view(), name="advertisement_add"),
]

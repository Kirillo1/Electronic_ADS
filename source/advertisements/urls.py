from django.urls import path

from advertisements.views.advertisements import (IndexView, AdvertisementDetailView,
                                                 AdvertisementCreateView, AdvertisementUpdateView, ModeratorListView)

app_name = "advertisements"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('advertisement/<int:pk>/', AdvertisementDetailView.as_view(), name="advertisement_detail_view"),
    path('advertisement/add/', AdvertisementCreateView.as_view(), name="advertisement_add"),
    path('advertisement/<int:pk>/update/', AdvertisementUpdateView.as_view(), name="advertisement_update_view"),
    path('moderator/', ModeratorListView.as_view(), name="moderator_list_view"),

]

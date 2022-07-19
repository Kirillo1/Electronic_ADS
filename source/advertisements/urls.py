from django.urls import path

from advertisements.views.advertisements import (IndexView, AdvertisementDetailView,
                                                 AdvertisementCreateView, AdvertisementUpdateView,
                                                 ModeratorListView, ProfileAdvertisementDetailView,
                                                 AdvertisementRemoveFavoriteView)

app_name = "advertisements"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('advertisement/<int:pk>/', AdvertisementDetailView.as_view(), name="advertisement_detail_view"),
    path('advertisement/add/', AdvertisementCreateView.as_view(), name="advertisement_add"),
    path('advertisement/<int:pk>/update/', AdvertisementUpdateView.as_view(), name="advertisement_update_view"),
    path('advertisement/<int:pk>/favorite', AdvertisementRemoveFavoriteView.as_view(), name="favorites_ads"),
    path('moderator/', ModeratorListView.as_view(), name="moderator_list_view"),
    path('profile/<int:pk>/', ProfileAdvertisementDetailView.as_view(), name="profile_advertisement_detail_view"),
]

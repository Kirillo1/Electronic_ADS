from django.urls import path

from advertisements.views.advertisements import (IndexView, AdvertisementDetailView,
                                                 AdvertisementCreateView, AdvertisementUpdateView,
                                                 ModeratorListView, ProfileAdvertisementDetailView,
                                                 AdvertisementRemoveFavoriteView, AdvertisementFavoriteListView,
                                                 AdsLikeView, AdsUnlikeView)

app_name = "advertisements"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('advertisement/<int:pk>/', AdvertisementDetailView.as_view(), name="advertisement_detail_view"),
    path('advertisement/add/', AdvertisementCreateView.as_view(), name="advertisement_add"),
    path('advertisement/<int:pk>/update/', AdvertisementUpdateView.as_view(), name="advertisement_update_view"),
    path('advertisement/<int:pk>/favorite', AdvertisementRemoveFavoriteView.as_view(), name="favorites_ads"),
    path('advertisement/favorites', AdvertisementFavoriteListView.as_view(), name="favorites"),
    path('moderator/', ModeratorListView.as_view(), name="moderator_list_view"),
    path('profile/<int:pk>/', ProfileAdvertisementDetailView.as_view(), name="profile_advertisement_detail_view"),
    path('advertisement/<int:pk>/like', AdsLikeView.as_view(), name='like_ads'),
    path('advertisement/<int:pk>/unlike', AdsUnlikeView.as_view(), name='unlike_ads'),

]

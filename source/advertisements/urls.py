from django.urls import path

from advertisements.views import (IndexView, AdsDetailView, AdsCreateView, AdsUpdateView, AuthorAdsView,
                                  AdsRemoveFavoriteView, AdsFavoriteListView, AdsLikeView, AdsUnlikeView,
                                  AdsDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView,
                                  ModeratorListView, AdsModerPublishView, AdsModerRejectView)

app_name = "advertisements"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('ads/<int:pk>/', AdsDetailView.as_view(), name="ads_detail_view"),
    path('ads/add/', AdsCreateView.as_view(), name="ads_add"),
    path('ads/<int:pk>/update/', AdsUpdateView.as_view(), name="ads_update_view"),
    path('ads/<int:pk>/delete/', AdsDeleteView.as_view(), name="ads_delete_view"),
    path('ads/<int:pk>/favorite', AdsRemoveFavoriteView.as_view(), name="favorites_ads"),
    path('ads/favorites', AdsFavoriteListView.as_view(), name="favorites"),
    path('ads/<int:pk>/like', AdsLikeView.as_view(), name='like_ads'),
    path('ads/<int:pk>/unlike', AdsUnlikeView.as_view(), name='unlike_ads'),
    path('moderator/', ModeratorListView.as_view(), name="moderator_list_view"),
    path('author/<int:pk>/', AuthorAdsView.as_view(), name="author_ads_view"),
    path('moderator/<int:pk>/publish', AdsModerPublishView.as_view(), name="ads_publish_view"),
    path('moderator/<int:pk>/reject', AdsModerRejectView.as_view(), name="ads_reject_view"),
    path('ads/<int:pk>/comments/add/', CommentCreateView.as_view(), name="ads_comment_create"),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name="comment_update_view"),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name="comment_delete_view"),
]

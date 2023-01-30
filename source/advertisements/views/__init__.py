from advertisements.views.advertisements import (IndexView, AdsDetailView, AdsCreateView, AdsUpdateView,
                                                 AdsDeleteView, AuthorAdsView, AdsRemoveFavoriteView,
                                                 AdsFavoriteListView, AdsLikeView, AdsUnlikeView)

from advertisements.views.comments import CommentCreateView, CommentUpdateView, CommentDeleteView

from advertisements.views.moderator_ads_views import (ModeratorListView,
                                                      AdsModerPublishView,
                                                      AdsModerRejectView)

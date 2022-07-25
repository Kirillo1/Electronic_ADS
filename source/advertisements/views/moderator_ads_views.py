from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.utils import timezone

from advertisements.models import Advertisement


class ModeratorListView(PermissionRequiredMixin, ListView):
    permission_required = "is__staff"
    model = Advertisement
    context_object_name = 'advertisements'
    template_name = "advertisements/moderator_list_view.html"
    paginate_by = 5
    ordering = ["created_at"]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(
            status=Advertisement.TO_DELETE).filter(
            status=Advertisement.TO_MODERATE).select_related(
            'author', 'author__profile', 'category').order_by('-created_at')


class AdsModerPublishView(View):
    def post(self, request, *args, **kwargs):
        ads = get_object_or_404(Advertisement, pk=kwargs['pk'])
        if ads.status != Advertisement.PUBLISHED:
            ads.status = Advertisement.PUBLISHED
            ads.published_at = timezone.now()
            ads.save()
            answer = 'Опубликовано'
        else:
            answer = 'Уже было опубликовано'
        data = {
            "answer": answer
        }
        return JsonResponse(data, safe=False)


class AdsModerRejectView(View):
    def post(self, request, *args, **kwargs):
        ad = get_object_or_404(Advertisement, pk=kwargs['pk'])
        if ad.status != Advertisement.REJECTED:
            ad.status = Advertisement.REJECTED
            ad.save()
            answer = 'Отклонено'
        else:
            answer = 'Уже было отклонено'
        data = {
            "answer": answer
        }
        return JsonResponse(data, safe=False)

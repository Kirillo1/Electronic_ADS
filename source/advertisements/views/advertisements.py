from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView

from advertisements.forms import AdsForm, CommentForm
from advertisements.models import Advertisement, Comment
from advertisements.views.base import SearchView
from django.core.paginator import Paginator

User = get_user_model()


class IndexView(SearchView):
    model = Advertisement
    context_object_name = 'advertisements'
    template_name = "advertisements/index.html"
    paginate_by = 5
    search_fields = ["title__icontains"]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(
            status=Advertisement.TO_DELETE).filter(
            status=Advertisement.PUBLISHED).select_related(
            'author', 'category').order_by(
            '-published_at')


class AdsDetailView(DetailView):
    template_name = 'advertisements/ads_detail_view.html'
    model = Advertisement

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = self.object.comments.order_by("-created_at")
        context['comments'] = comments
        return context


class AdsCreateView(CreateView):
    model = Advertisement
    form_class = AdsForm
    template_name = "advertisements/ads_create.html"
    success_url = reverse_lazy('advertisements:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdsUpdateView(UpdateView):
    form_class = AdsForm
    template_name = "advertisements/ads_update.html"
    model = Advertisement

    def get_success_url(self):
        return reverse('advertisements:ads_detail_view', kwargs={'pk': self.object.pk})


class AdsDeleteView(PermissionRequiredMixin, DeleteView):
    model = Advertisement
    template_name = 'advertisements/ads_delete_view.html'
    success_url = reverse_lazy('advertisements:index')

    def has_permission(self):
        return self.request.user == self.get_object().author


class AuthorAdsView(DetailView):
    model = User
    template_name = 'advertisements/author_ads_view.html'
    context_object_name = 'advertisements'
    paginate_related_by = 5
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        paginator = Paginator(
            self.get_object().advertisements.all(),
            self.paginate_related_by,
            self.paginate_related_orphans,
        )

        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        kwargs['page_obj'] = page
        kwargs['advertisements'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()

        return super(AuthorAdsView, self).get_context_data(**kwargs)


class AdsRemoveFavoriteView(View):
    def get(self, request, *args, **kwargs):
        try:
            favorite_ads = request.session["favorite_ads"]
        except KeyError:
            favorite_ads = []

        ads_id = kwargs.get("pk")

        if ads_id in favorite_ads:
            favorite_ads.pop(favorite_ads.index(ads_id))
        else:
            favorite_ads.append(ads_id)

        request.session["favorite_ads"] = favorite_ads
        redirect_to = reverse("advertisements:ads_detail_view", kwargs={"pk": ads_id})
        return HttpResponseRedirect(redirect_to)


class AdsFavoriteListView(ListView):
    model = Advertisement
    template_name = "advertisements/favorite.html"
    context_object_name = "advertisements"

    def get_queryset(self):
        favorite_ads_ids = self.request.session.get("favorite_ads", [])
        return self.model.objects.filter(id__in=favorite_ads_ids)


class AdsLikeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        ads = get_object_or_404(Advertisement, pk=kwargs.get('pk'))
        if request.user in ads.likes.all():
            return JsonResponse(
                {"error": "Лайк уже поставлен"},
                status=HTTPStatus.FORBIDDEN,
            )
        ads.likes.add(request.user)
        return JsonResponse(
            {"likes_count": ads.likes.count()}
        )


class AdsUnlikeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        ads = get_object_or_404(Advertisement, pk=kwargs.get('pk'))

        if not ads.likes.filter(id=request.user.id).exists():
            return JsonResponse(
                {"error": "Нужно сначала поставить лайк"},
            )
        ads.likes.remove(request.user)
        return JsonResponse(
            {"likes_count": ads.likes.count()}
        )

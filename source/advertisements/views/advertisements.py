from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, ListView

from advertisements.forms import AdvertisementForm
from advertisements.models import Advertisement
from advertisements.views.base import SearchView
from django.core.paginator import Paginator


class IndexView(SearchView):
    model = Advertisement
    context_object_name = 'advertisements'
    template_name = "advertisements/index.html"
    paginate_by = 5
    search_fields = ["title__icontains", "author__icontains"]
    ordering = ["-created_at"]


# def get_queryset(self):
#      queryset = super(IndexView, self).get_queryset()
#      return queryset.filter(status='published')

class AdvertisementDetailView(DetailView):
    template_name = 'advertisements/advertisement_detail_view.html'
    model = Advertisement


class AdvertisementCreateView(CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = "advertisements/advertisement_create.html"
    success_url = reverse_lazy('advertisements:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdvertisementUpdateView(UpdateView):
    # permission_required = "webapp.change_article"
    form_class = AdvertisementForm
    template_name = "advertisements/advertisement_update.html"
    model = Advertisement

    def get_success_url(self):
        return reverse('advertisements:advertisement_detail_view', kwargs={'pk': self.object.pk})

    # def has_permission(self):
    #     return self.get_object().author == self.request.user


class ModeratorListView(PermissionRequiredMixin, ListView):
    permission_required = "is__staff"
    model = Advertisement
    context_object_name = 'advertisements'
    template_name = "advertisements/moderator_list_view.html"
    paginate_by = 5
    ordering = ["created_at"]

    def get_queryset(self):
        queryset = super(ModeratorListView, self).get_queryset()
        return queryset.filter(status='for_moderation')


class ProfileAdvertisementDetailView(DetailView):
    model = get_user_model()
    template_name = 'advertisements/profile_advertisement_detail_view.html'
    context_object_name = 'profile'
    paginated_by = 4
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        profile = self.get_object().profile
        print(profile)
        paginator = Paginator(
            profile.advertisements.filter(status='published'),
            self.paginated_by,
            self.paginate_related_orphans
        )
        page_number = self.request.GET.get('page', '1')
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['advertisements'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super(ProfileAdvertisementDetailView, self).get_context_data(**kwargs)


class AdvertisementRemoveFavoriteView(View):
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
        redirect_to = reverse("advertisements:advertisement_detail_view", kwargs={"pk": ads_id})
        return HttpResponseRedirect(redirect_to)

from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from advertisements.forms import AdvertisementForm
from advertisements.models import Advertisement
from advertisements.views.base import SearchView


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

    # def has_permission(self):
    #     return self.get_object().author == self.request.user

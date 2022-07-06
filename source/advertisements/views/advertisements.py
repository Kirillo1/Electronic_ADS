from django.views.generic import ListView

from advertisements.models import Advertisement


class IndexView(ListView):
    model = Advertisement
    context_object_name = 'advertisements'
    template_name = "advertisements/index.html"
    paginate_by = 5
    search_fields = ["title__icontains", "author__icontains"]
    ordering = ["-created_at"]

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        return queryset.filter(status='published')

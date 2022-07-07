from profile import Profile

from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.views.generic import DetailView

User = get_user_model()


class UserProfileView(DetailView):
    model = User
    template_name = "profile.html"
    context_object_name = "user_object"
    paginate_related_by = 3
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

        return super(UserProfileView, self).get_context_data(**kwargs)

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from advertisements.forms import CommentForm
from advertisements.models import Comment, Advertisement


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "comments/create_view.html"

    def form_valid(self, form):
        advertisement = get_object_or_404(Advertisement, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.advertisement = advertisement
        comment.save()
        return redirect('advertisements:ads_detail_view', pk=advertisement.pk)


class CommentUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "advertisements.change_comment"
    model = Comment
    template_name = 'comments/update_view.html'
    form_class = CommentForm

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse("advertisements:ads_detail_view", kwargs={"pk": self.object.advertisement.pk})


class CommentDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "advertisements.delete_comment"
    model = Comment

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("advertisements:ads_detail_view", kwargs={"pk": self.object.advertisement.pk})

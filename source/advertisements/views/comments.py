from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from advertisements.forms import CommentForm
from advertisements.models import Comment, Advertisement


class CommentCreateView(CreateView):
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


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comments/update_view.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse("advertisements:ads_detail_view", kwargs={"pk": self.object.advertisement.pk})


class CommentDeleteView(DeleteView):
    model = Comment

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("advertisements:ads_detail_view", kwargs={"pk": self.object.advertisement.pk})

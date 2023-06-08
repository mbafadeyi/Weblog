from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import Post


class HomeView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"


# class DetailView(DetailView):
#     model = Post
#     template_name = "blog/post_detail"
def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status="published")
    related = Post.objects.filter(author=post.author)[:5]
    return render(request, "blog/detail.html", {"post": post, "related": related})

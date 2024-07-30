from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, CreateView  # , FormView
from django.shortcuts import get_object_or_404
# from django.http import HttpResponse

from .models import Post
from .forms import PostForm


# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        return context


class RedirectToMaktab(RedirectView):
    url = "https://maktabkhooneh.org"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostList(ListView):
    # queryset = Post.objects.all()
    model = Post
    context_object_name = "posts"
    # paginate_by = 2
    ordering = "-id"

    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts


class PostDetailView(DetailView):
    model = Post


"""
class PostCreateView(FormView):
    template_name = 'blog/contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    success_url = "/blog/post/"


@api_view()
def api_post_list_view(request):
    return Response("hi")

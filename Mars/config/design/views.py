
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import DescriptionPost, Post


def home(request):
    posts = Post.objects.all()
    post = DescriptionPost.objects.all()
    return render(request, 'base.html', {"post": post, "posts": posts})





#def Post_def(request):
#    post = DescriptionPost.objects.all()
#    return render(request, 'design/list_details.html', {'post': post})

    def get_queryset(self):
        return DescriptionPost.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


#def Post_detail(request):
#    post = DescriptionPost.objects.all()
#    return render(request, 'design/post_detail.html', {"post": post})


#class PostListView(DetailView):
#    model = Post
#    template_name = 'design/post_list.html'
#    context_object_name = 'data'

#def detail_post(request, slug, pk):
#    detail = get_object_or_404(Post, slug=slug, pk=pk)
#    context = {'detail': detail}
#    return render(request, 'design/list_details.html', context)

class PostDetail(DetailView):
    model = Post
    template_name = 'design/list_details.html'
    slug_url_kwarg = 'posts_slug'
    context_object_name = 'detail'



class DetaView(DetailView):
    model = DescriptionPost
    template_name = 'design/post_detail.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'



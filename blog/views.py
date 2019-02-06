from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView

from .models import Blog
from .forms import BlogModelForm

def blog(request):
    blogs = Blog.objects.all().order_by('pk').reverse()
    return render(request, 'blog/home.html', {'blogs': blogs, 'activate': 'blog'})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog' : blog, 'activate': 'blog'})

class PostCreateView(CreateView):
    # template_name = 'blog/blog_form.html' # App이름_form.html 을 자동으로 찾아서 보여줌
    model = Blog
    form_class = BlogModelForm

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['activate'] = 'create'
        return context
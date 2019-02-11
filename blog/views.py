from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.core.paginator import Paginator
from django.utils.timezone import datetime

from .models import Blog
from .forms import BlogModelForm

def blog(request):
    blogs = Blog.objects.all().order_by('pk').reverse()
    # 페이지로 나누기 
    paginator = Paginator(blogs, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'blog/home.html', {'posts': posts, 'activate': 'blog'})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog' : blog, 'activate': 'blog'})


class BlogCreateView(CreateView):
    # # "App이름_form.html" 을 자동으로 찾아서 보여줌
    # template_name = 'blog/blog_form.html' 
    # 모델 자체에 get_absolute_url 함수가 있다면 이 함수 호출로 대신
    # success_url = 'blog/' 
    model = Blog
    form_class = BlogModelForm

    # 기본찾아오는 템플릿인 "App이름_form.html" 에서 _form 을 _creat_form 으로 바꿔줌 
    template_name_suffix = '_create_form' 

    def get_context_data(self, **kwargs):
        context = super(BlogCreateView, self).get_context_data(**kwargs)
        context['activate'] = 'create'
        return context

        
""" 
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))
""" 
""" 
from django.http import HttpResponse, HttpResponseRedirect
def create2(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = datetime.now()
            post.save()
            print(post.id)
            # return redirect(reverse('detail', kwargs={'blog_id': post.id}))
            # return redirect('detail', post.id)
            return redirect(post)
    form = BlogModelForm()
    return render(request, 'blog/blog_create_form.html', {'form': form })
""" 
from django.shortcuts import render,redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.
def tampilan_blog(request):
    blog = Blog.objects.all()
    return render(request, 'Blog/tampilan_blog.html', {'blogs' : blog})

def input_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            #post = form.save
            form.save()
            return redirect('blog')
    else :
        form = BlogForm()
    return render(request, 'Blog/blog_form.html', {'form' : form})
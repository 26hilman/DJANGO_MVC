from django.shortcuts import render

# Create your views here.
def tampilan_blog(request):
    return render(request, 'Blog/tampilan_blog.html')


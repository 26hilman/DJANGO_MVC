from django.shortcuts import render

# Create your views here.
def tampilan_author(request):
    return render(request, 'Author/tampilan_author.html', {})
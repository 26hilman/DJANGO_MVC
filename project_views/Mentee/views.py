from django.shortcuts import render

# Create your views here.
def tampilan_mentee(request):
    return render(request, 'Mentee/tampilan_mentee.html', {})
from django.shortcuts import render

# Create your views here.
def tampilan_mentor(request):
    return render(request, 'Mentor/tampilan_mentor.html')
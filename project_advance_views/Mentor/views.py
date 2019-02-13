from django.shortcuts import render
from .models import Mentor

# Create your views here.
def tampilan_mentor(request):
    mentor = Mentor.objects.all()
    return render(request, 'Mentor/tampilan_mentor.html', {'mentors' : mentor})
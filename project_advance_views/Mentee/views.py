from django.shortcuts import render
from .models import Mentee

# Create your views here.
def tampilan_mentee(request):
    mentee = Mentee.objects.all()
    return render(request, 'Mentee/tampilan_mentee.html', {'mentees' : mentee})


# Create your views here.
from django.shortcuts import render

from core.forms import TodoForm



def home(request):
    form = TodoForm
    return render(request,'home.html', { 'forms': form })
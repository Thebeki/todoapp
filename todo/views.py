from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from .forms import *
from .models import * 

def index(request): 
      a = Post.objects.all()
      return render(request, "todo/home.html", {"f": a})
def todo(request):
  if request.method == "GET": 
      forma = TodoForm() 
  else: 
      down = TodoForm(request.POST) 
      if down.is_valid(): 
        f = down.cleaned_data
        Post.objects.create(
          title=f["title"], 
          plan = f['plan'],
          date = f['date'])
        return redirect('homepage')
     

  return render(request, "todo/form.html" , {"forma" : forma}) 




from django.shortcuts import render
from django.http import HttpResponse
from .models import Temperateur
    # Create your views here.

 #def index(request):
     # return render(request,'pages/index.html')
      # pass
#def home (request):
     # boards = Temperateur.objects.all()
      #boards_names = []
      #for temperateur in boards : 
       #     boards_names.append(temperateur.lat)
     # print(boards_names)
      #return HttpResponse(boards_names)



def home (request):
  #  boards = Temperateur.objects.all()[:15]
    boards = Temperateur.objects.all()[0:33000:1]
    
    return render(request,'home.html',{'boards':boards})
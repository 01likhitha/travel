from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=team.objects.all()
    return render(request,"index.html",{'result' : obj,'result1' : obj1})

# def operations(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     mult=x*y
#     sub=x-y
#     div=x/y
#     return render(request,"result.html",{"addition":add,"multiplication":mult,"subtraction":sub,"divsn":div})
# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return render(request,"contact.html")
# def details(request):
#     return render(request,"details.html")
# def thanks(request):
#     return HttpResponse("thank you")
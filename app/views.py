from django.shortcuts import render

# Create your views here.
def scientist(request):
    return render(request,'scientist.html')
def nature(request):
    return render(request,'nature.html')

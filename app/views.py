from django.shortcuts import render

# Create your views here.

def loops(request):
    d={'name':'MAHESH'}
    return render(request,'loops.html',context=d)

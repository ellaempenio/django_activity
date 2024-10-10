from django.shortcuts import render

# Create your views here.

def indexss(request):
    context={}
    return render(request, "myapp2/indexss.html", context )

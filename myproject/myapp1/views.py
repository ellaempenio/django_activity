from django.shortcuts import render

# Create your views here.
def shop(request):
    context={}
    return render(request, "myapp1/shop.html", context )

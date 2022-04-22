from django.shortcuts import render

# Create your views here.
def gethomepage(request):
    return render(request,'homepage/index.html')
    
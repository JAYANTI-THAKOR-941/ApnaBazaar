from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'main/index.html')

def Products(request):
    return render(request,'main/products.html')

def About(request):
    return render(request,'main/about.html')

def Contact(request):
    return render(request,'main/contact.html')


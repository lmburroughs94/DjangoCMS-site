from django.shortcuts import render
  
def base(request):
    return render(request, "base.html")
  
def about(request):
    return render(request, "about.html")
  
def contact(request):
    return render(request, "contact.html")

def pricing(request):
    return render(request, "pricing.html")

def faq(request):
    return render(request, "faq.html")

def blog_home(request):
    return render(request, "blog-home.html")
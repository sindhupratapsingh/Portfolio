from django.http import HttpResponse, HttpResponseRedirect


from django.shortcuts import render
from django.shortcuts import redirect,render
# from .forms  import ContactForm


def BASE(request):
    return render(request,'base.html')

def HOME(request):
    return render(request,'main/home.html')

def ABOUTUS(request):
    return render(request,'main/aboutus.html')

def CONTACT(request):
    return render(request,'main/contact.html')

def PROJECT(request):
    return render(request,'main/project.html')

def CV(request):
    
    return render(request,'main/cv.html')


# def Contactform(request):
#     if request.method=="POST":
#         form=ContactForm(request.POST)
#         if form.is_valid():
#             return
#             HttpResponseRedirect("/thanks/")  

#         else:
#             form=ContactForm()
#         return render(request,"main/contact.html",{"form":form})

    
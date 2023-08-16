from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from .forms import PersonRegistration,PersonLogin,PostCreate,Contactform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from .models import Post
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.core.cache import cache
# Home
def home(request):
     post = Post.objects.all()
     return render(request,'blogging/home.html',{'posts':post})
# Registration
def registration(request):
     if not request.user.is_authenticated:
        if request.method=='POST':
            fm = PersonRegistration(request.POST)
            if fm.is_valid():
                 user = fm.save()
                 group = Group.objects.get(name='User')
                 user.groups.add(group)
                 messages.success(request,'You are registerd successfully')
        else :  fm = PersonRegistration()
        return render(request,'blogging/registration.html',{'forms':fm})
     else:
         return HttpResponseRedirect('/dashboard/')
# ḷogin
def sign_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = PersonLogin(request=request,data= request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/dashboard/')
        
        else :
            fm = PersonLogin()
        return render(request,'blogging/login.html',{'forms':fm})
    else :
        return HttpResponseRedirect('/dashboard/')

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/sign_in/')

# dashboard
def dashboard(request):
    if request.user.is_authenticated:
        post = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        ip = request.session.get('ip',0)
        ch = cache.get('count',version=user.pk)

        return render(request,'blogging/dashboard.html',{'posts':post,'full_name':full_name,'groups':gps,'ip':ip,'ch':ch})

    else :
       return  HttpResponseRedirect('/sign_in/')


# About Section
def about(request):
    return render(request,'blogging/about.html')

    # Adding a PostCreate
def addpost(request):
     
      if request.method=='POST':
            fm = PostCreate(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Congartulations! Article is Published. Click on cancle for go back to home')
      else :  fm = PostCreate()
      return render(request,'blogging/addpost.html',{'forms':fm})

def updatepost(request,id):     
      if request.method=='POST':
            pi = Post.objects.get(pk=id)
            fm = PostCreate(request.POST,instance=pi)
            if fm.is_valid():
                title = fm.cleaned_data['title']
                desc = fm.cleaned_data['desc']
                user = Post(id=id,title=title,desc=desc)
                user.save()
                messages.success(request,'Article is Updated Successfully')
                        
      else : 
          pi = Post.objects.get(pk=id)
          fm = PostCreate(instance=pi)
      return render(request,'blogging/updatepost.html',{'forms':fm})
def deletepost(request,id):  
    if request.method=='POST':
            fm = Post.objects.get(pk=id)
            fm.delete()

def read_article(request,id):
    post = Post.objects.get(pk=id)
    return render(request,'blogging/article.html',{'posts':post})

def contact_us(request):
    if request.method=='POST':
        fm = Contactform(request.POST)
        if fm.is_valid():
            name  = fm.cleaned_data['name']
            email_from  =settings.EMAIL_HOST_USER
            query  = fm.cleaned_data['query']
            recipient_list= ['abhishekudiya2000@gmail.com',]
            try:
                send_mail('User wants to contact', query, email_from, recipient_list,fail_silently=False)
                messages.success(request, f'Thank you {name} for contacting us. We will reach out to you as soon as possible.')
            except Exception as e:
                messages.error(request, 'An error occurred while sending the email. Please try again later.')

            return redirect('/contact/')
    else : fm = Contactform()
    return  render(request,'blogging/contact.html',{'forms':fm})
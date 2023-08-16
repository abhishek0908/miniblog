from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache

@receiver(user_logged_in,sender = User)
def logged_success(sender,request,user,**kwargs):
    print("---------------")
    print("Logged-in Signal... Run Intro")
    ip =  request.META.get('REMOTE_ADDR')
    print("Client Ip:",ip)
    request.session['ip']=ip

@receiver(user_logged_in,sender = User)
def logged_success(sender,request,user,**kwargs):
    print("---------------")
    print("Logged-in Count.. Run Intro")
    ch =  cache.get('count',0,version=user.pk)
    newch = ch+1
    cache.set('count',newch,60*60*24,version=user.pk)
    print(newch)


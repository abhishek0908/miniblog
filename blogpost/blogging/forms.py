from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django import forms
from .models import Post

class PersonRegistration(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Enter Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
        labels = {'username':'Enter UserName','first_name':'Enter First Name','last_name':'Enter Last Name','email':'Enter Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'})}


class PersonLogin(AuthenticationForm):
   username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
   password = forms.CharField(label='Password', strip = False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class PostCreate(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['title','desc']
        labels = {'title':'Title','desc':'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),'desc':forms.Textarea(attrs={'class':'form-control'})}



class Contactform(forms.Form):
     name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
     query = forms.CharField(label='Ask Question', widget=forms.Textarea(attrs={'class': 'form-control'}))

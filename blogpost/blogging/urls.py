from django.urls import path
from . import views
urlpatterns = [

        path('',views.home,name='home'),
        path('sign_up/',views.registration,name ='sign_up' ),
        path('about/',views.about,name ='about' ),
        path('sign_in/',views.sign_in,name ='sign_in' ),
        path('dashboard/',views.dashboard,name ='dashboard' ),
        path('logout/',views.user_logout,name ='logout' ),
        path('addpost/',views.addpost,name ='addpost' ),
        path('updatepost/<int:id>/',views.updatepost,name ='updatepost' ),
        path('deletepost/<int:id>/',views.deletepost,name ='deletepost' ),
        path('contact/',views.contact_us,name ='contact' ),
        path('article/<int:id>/',views.read_article,name ='article' ),

]
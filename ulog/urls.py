from django.urls import path
from .views import home,signin,signout,signup

urlpatterns = [
    path('',signin,name='signin'),
    path('home/',home,name='home'),
    path('logout/',signout,name='signout'),
    path('singup/',signup,name='signup'),
]

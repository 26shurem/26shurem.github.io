from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('login_user', views.login_user,name="login_user"),
    path('logout', views.logout_user,name="logout_user"),
    path('contact',views.contacts,name='contacts'),
    path('join',views.Enroll,name='enroll')
]

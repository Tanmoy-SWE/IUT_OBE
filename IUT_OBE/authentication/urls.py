from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='LoginPage'),
    path('register', views.register, name="register"),
    path('logout', views.logout_user, name="logout"),
    path('addCourse', views.add_course, name="addCourse"),
    path('sessionList/<pk>', views.session_list, name="sessionlist"),
    #path('addSession/<pk>', views.add_session, name="addsession"),

    
]
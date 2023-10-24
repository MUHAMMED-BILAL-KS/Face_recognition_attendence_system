from django.urls import path
from . views import *
from django.conf.urls.static import static
from project import settings

urlpatterns = [
    path('',home,name='index'),
    path('profiles/',profiles,name='profiles'),
    path('register/',register,name='register'),
    path('attendence/',attendence,name='attendence'),
    path('delete/<int:id>/',deleteprofile,name='delete'),
    path('modify/<int:id>/',modifyprofile,name='modify'),
    path('profilepresent/<int:id>/',profilepresent,name='profilepresent'),
    path('profileabsent/<int:id>/',profileabsent,name='profileabsent'),
    path('scan/',scan,name='scan'),
    path('reset1/',reset1,name='reset1'),
    path('save1/',save1,name='save1'),
    path('send_email/',send_email,name='send_email'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

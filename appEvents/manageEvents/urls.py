
from django.urls import  path
from manageEvents import views


urlpatterns = [
    path('',views.home, name="Home"),
    path('contactus/',views.contactus, name="ContactUs"),
    path('addEvent/', views.addEvents, name="addEvent"),
    path('readEvent/', views.readEvents, name="readEvents"),
    path('modifyEvent/<id>/', views.modify_event, name="modifyEvent"),
    path('deleteEvent/<id>/', views.deleteEvent, name="deleteEvent"),
    path('userRegistration/', views.userRegister, name="userRegistration" ),
    path('eventDetails/<id>/', views.view_events, name="eventDetails" ),
    path('subscribe_event/', views.subscribe_event, name="subscribe_event" ), 
]



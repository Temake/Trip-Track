from django.shortcuts import render
from django.urls import path
from .views import Homeview,tripslist,TripCreate,Tripdetailview,NoteDetail,Notelistview,NoteCreateView

urlpatterns =[
    path('', Homeview.as_view(), name='home'),
    path('dashboard/',tripslist, name= 'trip-list'),
    path('dashboard/notes/',Notelistview.as_view(), name= 'note-list'),
    path('dashboard/notes/create',NoteCreateView.as_view(), name= 'note-create'),
    path('dashboard/trips/create',TripCreate.as_view(), name= 'trip-create'),
    path('dashboard/trips/<int:id>/',Tripdetailview.as_view(), name= 'trip-detail'),
    path('dashboard/notes/<int:id>/',NoteDetail.as_view(), name= 'note-detail')
]





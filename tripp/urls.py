from django.shortcuts import render
from django.urls import path
from .views import Homeview,tripslist,TripCreate,Tripdetailview,NoteDetail,Notelistview,NoteCreateView,NoteDeleteView,NoteUpdateView,TripUpdateView,TripDeleteView

urlpatterns =[
    path('', Homeview.as_view(), name='home'),
    path('dashboard/',tripslist, name= 'trip-list'),
    path('dashboard/notes/',Notelistview.as_view(), name= 'note-list'),
    path('dashboard/notes/create',NoteCreateView.as_view(), name= 'note-create'),
    path('dashboard/trips/create',TripCreate.as_view(), name= 'trip-create'),
    path('dashboard/trips/<int:id>/',Tripdetailview.as_view(), name= 'trip-detail'),
    path('dashboard/notes/<int:id>/',NoteDetail.as_view(), name= 'note-detail'),
    path('dashboard/notes/<int:id>/update/',NoteUpdateView.as_view(), name= 'note-update'),
    path('dashboard/notes/<int:id>/delete/',NoteDeleteView.as_view(), name= 'note-delete'),
    path('dashboard/trips/<int:id>/update/',TripUpdateView.as_view(), name= 'trip-update'),
    path('dashboard/trips/<int:id>/delete/',TripDeleteView.as_view(), name= 'trip-delete'),
]





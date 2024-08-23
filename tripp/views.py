from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView
from .models import Trip,Note

# Create your views here.
class Homeview(TemplateView):
    template_name='tripp/index.html'

def tripslist(request):
    trips = Trip.objects.filter(owner=request.user)
    context={
        'trips':trips
    }
    return render (request,'tripp/trip_list.html',context)

class TripCreate(CreateView):
    model= Trip
    success_url = reverse_lazy('trip-list')
    fields= ['city','country','start_date','end_date']

    def form_valid(self, form):
        form.instance.owner= self.request.user
        return super().form_valid(form)
    
class Tripdetailview(DetailView):
    model = Trip  
    def get_object(self):
        return Trip.objects.get(id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        trip =context['object']
        notes = trip.notes.all()
        context['notes']=notes
        return context
class NoteDetail(DetailView):
    model= Note
    def get_object(self):
        return Note.objects.get(id=self.kwargs['id'])

class Notelistview(ListView):
    model =Note

    def get_queryset(self):
        queryset=Note.objects.filter(trip__owner=self.request.user)
        return queryset
class NoteCreateView(CreateView):
    model =Note
    success_url=reverse_lazy('note-list')
    fields= '__all__'

    def get_form(self):
        form = super(NoteCreateView,self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form
class NoteUpdateView(UpdateView):
    model =Note
    fields= '__all__'
    success_url=reverse_lazy('note-list')

    def get_object(self):
        return Note.objects.get(id=self.kwargs['id'])

    
    def get_form(self):
        form = super(NoteUpdateView,self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form
    
class NoteDeleteView(DeleteView):
    model =Note
    success_url=reverse_lazy('note-list')
    def get_object(self):
        return Note.objects.get(id=self.kwargs['id'])
class TripUpdateView(UpdateView):
    model = Trip
    fields = ['city', 'country', 'start_date', 'end_date']
    success_url = reverse_lazy('trip-list')

    def get_object(self):
        return Trip.objects.get(id=self.kwargs['id'])

class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy('trip-list')

    def get_object(self):
        return Trip.objects.get(id=self.kwargs['id'])

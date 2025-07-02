from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import EventForm
from .models import Event
from datetime import datetime


# Create your views here.
def Home(request):
    return render(request, 'Events/Home.html')

def register(request):
    if request.method == 'POST':    
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user=authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Events/Register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('event_list')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'Events/Login.html', {'form': AuthenticationForm()})


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'Events/Add_Event.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('home')

@login_required
def event_list_view(request):
    events = Event.objects.filter(organizer=request.user).order_by('-date')
    return render(request, 'Events/My_Events.html', {'events': events})

@login_required
def edit_event_view(request, event_id):

    event = get_object_or_404(Event, id=event_id)
    if event.organizer != request.user:
        messages.error(request, 'You do not have permission to edit this event.')
        return redirect('event_list')
     # Handle form submission
     # If the request method is POST, it means the user is submitting the form to update the event
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'Events/Add_event.html', {'form': form,})

@login_required
def delete_event_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.organizer != request.user:
        messages.error(request, 'You do not have permission to delete this event.')
        return redirect('event_list')
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('event_list')
    return render(request, 'Events/Delete_Event.html', {'event': event})

def events_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
   
    return render(request, 'Events/Events_Detail.html', {'event': event})

def upcoming_events_view(request):
    events = Event.objects.filter(date__gte=datetime.now()).order_by('date')
    return render(request, 'Events/Upcoming.html', {'events': events})




from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from event_app.models import *

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email') 
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        user_exist = EventUserModel.objects.filter(username = username).exists()
        
        if user_exist:
            messages.warning(request, "This username already exists")
            return redirect('sign_up')
        
        if password == confirm_password:
            EventUserModel.objects.create_user(
                username = username,
                email = email,
                full_name = full_name,
                phone_number = phone_number,
                password = password
            )
            messages.success(request, "Account Created Successfully")
            return redirect('sign_in')
        else:
            messages.warning(request, "Your Password Does Not Match")
            return redirect('sign_up')
    return render(request, 'sign_in/sign-up.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_id = authenticate(username = username, password = password)
        if user_id:
            login(request, user_id)
            messages.success(request, "Welcome to Event Management")
            return redirect('dash_board')
        else:
            messages.warning(request, "Your username or credential does not match")
            return redirect('sign_in')
    return render(request, 'sign_in/sign-in.html')

@login_required
def sign_out(request):
    logout(request)
    return redirect('sign_in')

@login_required
def dash_board(request):
    events = EventModel.objects.all()
    filter_data = request.GET.get('search')
    if filter_data:
        events = EventModel.objects.filter(
            Q(event_title__icontains = filter_data) |
            Q(event_type__icontains = filter_data) |
            Q(event_location__icontains = filter_data)
        )
    context = {
        'events' : events
    }
    return render(request, 'dashboard.html', context)

@login_required
def my_event(request):
    events = EventModel.objects.all()
    filter_data = request.GET.get('status')
    if filter_data:
        events = EventModel.objects.filter(event_status = filter_data)
    context = {
        'events' : events,
        'filter_data': filter_data
    }
    return render(request, 'events/my-event.html', context)

@login_required
def individual_event(request, e_id):
    event = EventModel.objects.get(id = e_id)
    context = {
        'event' : event
    }
    return render(request, 'events/single-event.html', context)

@login_required
def add_new_event(request):
    if request.method == 'POST':
        event_title = request.POST.get('title')
        event_type = request.POST.get('type')
        event_description = request.POST.get('description')
        event_date = request.POST.get('date')
        event_status = request.POST.get('status')
        event_location = request.POST.get('location')
        event_image = request.FILES.get('photo')
        
        EventModel.objects.create(
            event_title = event_title,
            event_type = event_type,
            event_description = event_description,
            event_date = event_date,
            event_status = event_status,
            event_location = event_location,
            event_image = event_image,
        )
        messages.success(request, "New Event Added Successfully")
        return redirect('dash_board')
    return render(request, 'events/add-event.html')

@login_required
def update_event(request, e_id):
    events = EventModel.objects.get(id = e_id)
    if request.method == 'POST':
        event_title = request.POST.get('title')
        event_type = request.POST.get('type')
        event_description = request.POST.get('description')
        event_date = request.POST.get('date')
        event_status = request.POST.get('status')
        event_location = request.POST.get('location')
        event_image = request.FILES.get('photo')
        
        events.event_title = event_title
        events.event_type = event_type
        events.event_description = event_description
        events.event_date = event_date
        events.event_status = event_status
        events.event_location = event_location
        if event_image:
            events.event_image = event_image
        events.save()
        return redirect('my_event')
    context = {
        'events' : events
    }
    return render(request, 'events/update-event.html', context)

@login_required
def delete_event(request, e_id):
    EventModel.objects.get(id = e_id).delete()
    return redirect('my_event')

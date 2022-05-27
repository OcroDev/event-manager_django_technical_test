from django.shortcuts import render, redirect, get_object_or_404
from .models import Events
from .forms import ContactForm, addEvent, customUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required

# Create your views here.


#def login(request):
 #   return render(request, 'registration/login.html',)
 
def  home(request):
    events = Events.objects.all()
    data = {
        'events' : events,
        #'total': events.subscribe.count()
    }
    return render(request, 'app/home.html', data)


def contactus(request):
    data = {
        'form' : ContactForm()
    }

    if  request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            data["message"] = "Contact Saved"
        else:
            data["form"] = form
           
    return render(request, 'app/contactus.html', data)


@permission_required('manageEvents.add_events')
def addEvents (request):
    
    data = {
        'form' : addEvent()
    }

    if request.method == 'POST':
        form = addEvent(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event saved successfully")
            redirect(to="readEvents")
            #data["message"] = "Event saved successfully"
        else:
            data["form"] = form

    return render( request, 'app/crudEvents/add.html', data ) 

@permission_required('manageEvents.view_events')
def readEvents(request):

    events = Events.objects.all()

    page = request.GET.get( 'page', 1 )
   
    try:
        paginator = Paginator(events, 5)
        events = paginator.page(page)
    except: 
        raise Http404

#entity es la variable genérica para el uso de la plantilla del paginador

    data = {
        'entity': events,
        'paginator':paginator
    }
    return render( request, 'app/crudEvents/read.html', data )

@permission_required('manageEvents.change_events')
def modify_event(request, id):
    event = get_object_or_404(Events, id=id)
    data = {
      'form' : addEvent(instance=event)
    }
    if request.method == 'POST':
        form = addEvent(data=request.POST, instance=event)
        if form.is_valid():
            form.save()
            #data["message"] = "Event modified successfully"
            messages.success(request, "Event modified successfully")
            return redirect(to="readEvents")
        data["form"] = form
    return render( request, 'app/crudEvents/modify.html', data )

@permission_required('manageEvents.delete_events')
def deleteEvent(request, id):
    event = get_object_or_404(Events, id=id)
    event.delete()
    messages.success(request, "Event deleted successfully")
    return redirect(to="readEvents")
 
def userRegister(request):
    data = {
        'form': customUserCreationForm
    }

    if request.method == 'POST':
        form = customUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username= form.cleaned_data["username"], password=form.cleaned_data["password1"] )
            login(request, user)
            messages.success(request, "You have logged in correctly")
            #redirect
            return redirect (to="Home")
        data['form'] = form
    return render(request, 'registration/registration.html', data)

def view_events(request, id):
    event = get_object_or_404(Events, id=id)
    is_subscribed = False
    if event.subscribe.filter(id=request.user.id).exists():
        is_subscribed = True
    data = { 
        'event' : event, 
        'is_subscribed' : is_subscribed,
        'total_subs' :  event.total_subs() ,
        }
    return render( request, 'app/events_details.html', data)


def subscribe_event(request):
    event = get_object_or_404(Events, id=request.POST.get('event_id'))
    is_subscribed = False
    if event.subscribe.filter(id=request.user.id).exists():
        event.subscribe.remove(request.user)
        is_subscribed = False
    else:
        event.subscribe.add(request.user)
        is_subscribed = True
    return redirect(to="Home")

    #return HttpResponseRedirect(event.get_absolute_url())


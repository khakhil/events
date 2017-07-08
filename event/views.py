# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, ListView, View
from .models import ContactSubmissions, EventTypes, EventCategories, Events, Media, Speaker, Partners, Sponsers, EmailNewsletter, CategoriesOfEvents, TypesOfEvents, EventTypes
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.db import transaction, IntegrityError
from django.contrib import messages
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage  
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

class UserView(TemplateView):
    template_name = "event/user.html"
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST' and 'loginform' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
             
            user = authenticate(username=username, password=password)
            if user is not None:
                request.session.set_expiry(86400) #sets the exp. value of the session 
                login(request, user) #the user 
                user.last_login = timezone.now()
                return HttpResponseRedirect('/events/')
#                 if next == "":
#                     return HttpResponseRedirect('/events/')
#                 else:
#                     return HttpResponseRedirect(next)
            else:
                errors = ["Invalid username or password !!!"]
                return render(request, self.template_name, {'errors': errors})
            
        elif request.method == 'POST' and 'registerform' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
                 
            errors = []
                 
            if not errors:
                try:
                    try:
                        user = User.objects.get(username=email)
                        if user is not None:
                            errors = ["Username already exist.. please try another"]
                            return render(request, 'event/user.html', {'errors': errors})
                    except:  
                        User.objects.create_user(password=password, username=email, email=email, date_joined=timezone.now())
                        return HttpResponseRedirect('/user/')
     
                except Exception, err: 
                    return HttpResponse(str(err))
            return render(request, 'event/user.html', {'errors': errors})
             

    
@method_decorator(login_required, name='dispatch')   
class LogOut(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)
    
class EventsView(TemplateView):
    template_name = "event/event.html"
    model = Events
#         search = self.request.GET.get('search')
#         page = self.request.GET.get('page')
#          
#         if search is not None:
#             event_types = EventCategories.objects.all()
#                    
#             events_data = Events.objects.values('event_name', 'tag_line', 'logo', 'url_key').order_by('event_start_date')
#             events_data = events_data.filter(city=self.kwargs['city'])
#             paginator = Paginator(events_data, self.paginate_by)
#             try:
#                 file_exams = paginator.page(page)
#             except PageNotAnInteger:
#                 file_exams = paginator.page(1)
#             except EmptyPage:
#                 file_exams = paginator.page(paginator.num_pages)
#                
#             context['events'] = file_exams
#             context['event_types'] = event_types
#             context['num_page'] = paginator.num_pages
#         return render(self.request, 'event/event_detail.html',) 
        
    def post(self, request, *args, **kwargs):
        if request.method == 'POST' and 'searchform' in request.POST:
            keyword = request.POST.get('keyword')
            city = request.POST.get('city')
            event_types = EventCategories.objects.all()
            events_data = Events.objects.values('event_name', 'tag_line', 'logo', 'url_key').order_by('event_start_date')
            
            if city is not "" or keyword is not "":
                if city is not "":
                    events_data = events_data.filter(city=city)
                if city is not "":
                    events_data = events_data.filter(event_name=keyword)
                    
                return render(self.request, 'event/city_events.html',{'events':events_data, 'event_types':event_types})   
            
             
        elif request.method == 'POST' and 'newsfrm' in request.POST:
            email = request.POST.get('email')
            try:
                EmailNewsletter.objects.get(email=email)
                     
            except:  
                EmailNewsletter.objects.create(email=email)
                send_mail("Thank you connecting us",                                                   #subject
                    '''Hi !!!.
 
Welcome to events.com! Thanks so much for joining us. You’re on your way to super-productivity and beyond!.
Prioritizer is a task management app that helps you focus on the important things in life by only allowing you to add 3 items a day. Set and track daily, weekly, and monthly priorities — and get the stuff that matters done.
 
Our number one tip to get the most out of Prioritizer is to download our browser extension and give it a whirl. [how it helps] It’ll make sticking to your priorities super simple and just a click away.
 
Have any questions? Just shoot us an email! We’re always here to help.
 
Cheerfully yours,
The Events Team''',                                                                            #body
 
'johnfrancis012345@gmail.com',                                                                                  #server mail
 
[request.POST.get('email'),])   
            return HttpResponseRedirect('/events/')
        return HttpResponseRedirect('/events/')  
    
    def get(self, request, city=None):
        featured_events = Events.objects.filter(is_featured=1).values('event_name', 'tag_line', 'logo', 'url_key')[:8]
        context = {'featured_events': featured_events,}
        return render(request, 'event/event.html', context)
    
    
class Contact(TemplateView):
    template_name = "event/contactus.html"
    
    def post(self,request):
        errors=[]
        if request.method == 'POST':
            name = request.POST.get('name')
            mobile_no = request.POST.get('phone')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            if not name:
                errors.append('name is required')
            if not mobile_no:
                errors.append('Phone no. is required.')
            if email and '@' not in request.POST['email']:
                errors.append('Enter a valid e-mail address.')
            if not email:
                errors.append('email is required')
            if not subject:
                errors.append('subject is required')
            if not message:
                errors.append('message is required')
            if not errors:
                try:
                    message_success ="Your message sent successfully."
                    ContactSubmissions.objects.create(name=name, phone = mobile_no, email=email, subject=subject, message=message)
                    send_mail("Thank you connecting us",                                                   #subject
                    '''Dear Authors,                                                                       

Congratulations for being a part of the ETEMSD2016 International Conference. 
Please find attached the Schedule for 19th and 20th February 2016, and the Track wise details.

Please identify your Track, Date and Time and mark your presence accordingly.
Due to many quality Papers up for presentation, we request the Authors to prepare presentation of not more than 5-6 minutes per paper.

We look forward to share an intellectual experience with you.


Thanks and Regards,
Monika Shekhawat
ETEMSD2016 Organizing Committee.''',                                                                            #body

'johnfrancis012345@gmail.com',                                                                                  #server mail

[request.POST['email'],])   
                    return render(request, 'event/contactus.html', {'errors': errors, 'message_success':message_success,})   
                except Exception: 
                    return render(request, 'event/contactus.html',)
        return render(request, 'event/contactus.html',
            {'errors': errors})
    
# def CityEvent(request, city):
#     events_data = Events.objects.filter(city=city).values('event_name', 'tag_line', 'logo', 'url_key').order_by('event_start_date')
#     page = request.GET.get('page', 1)
#     event_types = EventCategories.objects.all()
#      
#     paginator = Paginator(events_data, 4)
#     try:
#         events = paginator.page(page)
#     except PageNotAnInteger:
#         events = paginator.page(1)
#     except EmptyPage:
#         events = paginator.page(paginator.num_pages)
#  
#     return render(request, 'event/city_events.html', { 'events': events, 'event_types':event_types })

class CityEvent(ListView):
    model = Events
    template_name = "event/city_events.html"
    paginate_by = 4
    
            
    def get_context_data(self, city=None, **kwargs):        
        context = super(CityEvent, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
          
        event_types = EventCategories.objects.all()
                  
        events_data = Events.objects.values('event_name', 'tag_line', 'logo', 'url_key').order_by('event_start_date')
        events_data = events_data.filter(city=self.kwargs['city'])
        paginator = Paginator(events_data, self.paginate_by)
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
          
        context['events'] = file_exams
        context['event_types'] = event_types
        context['num_page'] = paginator.num_pages
        return context
    
class EventType(TemplateView):
    model = Events
    template_name = "event/event_types.html"
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super(EventType, self).get_context_data(**kwargs)
        
        event_categories = EventTypes.objects.all()
        page = self.request.GET.get('page')
        cat_id = None
        cat = self.request.GET.get('cat')
        if self.kwargs['event_types'] is not None:
            event_cat_id = EventCategories.objects.filter(url_key=self.kwargs['event_types']).all()
            event_id  = CategoriesOfEvents.objects.filter(event_category=event_cat_id).all()
            
        events=[]
        if event_id is not None:
            for ev_id in event_id:
                event_types = Events.objects.filter(pk=ev_id.event_id, city=self.kwargs['city']).values('event_name', 'tag_line', 'logo', 'url_key').order_by('event_start_date')
                if len(event_types) > 0:
                    events.append(event_types[0])
                    
        if cat is not None:
            event_type_id = EventTypes.objects.filter(url_key=cat).all()
            cat_id  = TypesOfEvents.objects.filter(event_types=event_type_id).all()
           
        if cat_id is not None:
            events = [] 
            for c_id in cat_id:
                event_types = Events.objects.filter(pk=c_id.event_id, city=self.kwargs['city']).values('event_name', 'tag_line', 'logo', 'url_key').order_by('event_start_date')
                if len(event_types) > 0:
                    events.append(event_types[0])    
        
        paginator = Paginator(events, self.paginate_by)
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
            
        context['events'] = file_exams
        context['event_categories'] = event_categories
        context['num_page'] = paginator.num_pages
        context['cat'] = cat
        
           
        return context
    
class EventDetail(TemplateView):
    template_name = "event/event_detail.html"
    
    def get(self, request, event_url=None):
        event_data = Events.objects.filter(url_key=event_url).all()[0]
        speakers = Speaker.objects.filter(event_id=event_data.pk).all()
        partners = Partners.objects.filter(event_id=event_data.pk).all()
        sponsers = Sponsers.objects.filter(event_id=event_data.pk).all()
        featured_events = Events.objects.filter(is_featured=1).values('event_name', 'tag_line', 'logo', 'url_key')[:8]
        context = {'event_data': event_data, 'speakers':speakers, 'partners':partners, 'sponsers':sponsers, 'featured_events':featured_events}
        return render(request, 'event/event_detail.html', context)
        
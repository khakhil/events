from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

app_name = 'event'
urlpatterns = [
    url(r'^$', views.EventsView.as_view(), name='events'),
    url(r'^user/$', views.UserView.as_view(), name='user'),
    
    url('^', include('django.contrib.auth.urls')),
    url(r'^logout/$', views.LogOut.as_view(), name='logout'),
    url(r'^contact/$', views.Contact.as_view(), name='contact'),
    url(r'^events/(?P<city>.[A-Za-z]+)/$', views.CityEvent.as_view(), name='city'),
    url(r'^events/(?P<city>.[A-Za-z]+)/(?P<event_types>.*)/?(?P<event_filter>.*)/$', views.EventType.as_view(), name='event_types'),
    url(r'^event/index/(?P<event_url>.*)/$', views.EventDetail.as_view(), name='event_detail'),
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
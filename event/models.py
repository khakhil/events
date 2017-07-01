from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django import forms
from idlelib.IOBinding import blank_re
from django.template.defaultfilters import default
from enum import unique

class Blogs(models.Model):
    unique_display = models.CharField(max_length=200,blank=True, null=True)
    url_key = models.CharField(max_length=200,)  # for help text
    title = models.CharField(max_length=200,)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey('auth.User', blank=True, null=True)
    source = models.CharField(max_length=200,blank=True, null=True)
    status = models.CharField(max_length=200, choices=[('', ''), ('Draft', 'Draft'), ('Trash','Trash'), ('Published', 'Published')], default='Draft',blank=True, null=True)
    post_date = models.DateTimeField(default=timezone.now)
    views = models.PositiveIntegerField(blank=True, null=True)
    genre_cat = models.ForeignKey('GenreCategories', blank=True, null=True)
    post_type = models.CharField(max_length=200, choices=[('', ''),('Blog', 'Blog'), ('News', 'News')], default='Blog',blank=True, null=True)
    excerpt = models.CharField(max_length=200,blank=True, null=True)
    pic = models.ForeignKey('Media', blank=True, null=True)
    
    class Meta:
        db_table = "blogs"
        
class CategoriesOfEvents(models.Model):
    event = models.ForeignKey('Events')
    event_category = models.ForeignKey('EventCategories')
    
    class Meta:
        db_table = "categories_of_events"
        
class CategoriesOfEventManagers(models.Model):
    user = models.ForeignKey('auth.User')
    event_category = models.ForeignKey('EventCategories')
    
    class Meta:
        db_table = "categories_of_event_managers"
        
class CiSessions(models.Model):
    ip_address = models.CharField(max_length=200,blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    data = models.CharField(max_length=200,blank=True, null=True)
    
    class Meta:
        db_table = "ci_sessions"
        
class ContactSubmissions(models.Model):
    name = models.CharField(max_length=200,)
    email = models.EmailField(max_length=200, blank=False)
    phone = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '0 to 9'. Up to 10 digits allowed.")], blank=True)
    message = models.TextField(blank=True, null=True)
#     agent = models.ForeignKey('Agent')
    submit_time = models.DateTimeField(default=timezone.now)
    subject = models.CharField(max_length=200,)
    
    class Meta:
        db_table = "contact_submissions"
        
class Countries(models.Model):
    sortname = models.CharField(max_length=3,)
    name = models.CharField(max_length=200,)
    url_key = models.CharField(max_length=200, blank=True)
    
    class Meta:
        db_table = "countries"

class CurlEventUrl(models.Model):
    url = models.CharField(max_length=200,)
    
    class Meta:
        db_table = "curl_event_url"
        
class EmailNewsletter(models.Model):
    email = models.EmailField(max_length=200, blank=False, unique=True)
    date = models.DateField(default=timezone.now)
    
    class Meta:
        db_table = "email_newsletter"
        
class Enquiries(models.Model):
    name = models.CharField(max_length=200,)
    email = models.EmailField(max_length=200, blank=False)
    phone = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '0 to 9'. Up to 10 digits allowed.")], blank=True)
    message = models.TextField(blank=True, null=True)
    property = models.ForeignKey('PropertyTypes', blank=True, null=True)
    rent_or_sale = models.CharField(max_length=200,choices=[('Rent', 'Rent'), ('Sale','Sale')], )
    country = models.ForeignKey('Countries', blank=True, null=True)
    city = models.CharField(max_length=200,)
    property_type = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=200,)
    price = models.FloatField(null=True)
    zip = models.CharField(max_length=10,)
#     agent = models.ForeignKey('Agent') 
    date = models.DateField(default=timezone.now)
    user_ip = models.CharField(max_length=100,)
    
    class Meta:
        db_table = "enquiries"
        
class Events(models.Model):
    event_name = models.CharField(max_length=200,)
    tag_line = models.CharField(max_length=200,)
    event_start_date = models.DateField(blank=True)
    event_start_time = models.TimeField(blank=True)
    event_end_date = models.DateField(blank=True)
    event_end_time = models.TimeField(blank=True)
    logo = models.CharField(max_length=200,blank=True, null=True)
    banner_1_event = models.CharField(max_length=200,blank=True, null=True)
    banner_2_event = models.CharField(max_length=200,blank=True, null=True)
    banner_3_event = models.CharField(max_length=200,blank=True, null=True)
    event_description = models.TextField(blank=True, null=True)
    organizer = models.CharField(max_length=200, blank=True, null=True)
    country =  models.ForeignKey('Countries')
    city = models.CharField(max_length=200, blank=True, null=True)
    address_line_1 = models.CharField(max_length=200, blank=True, null=True)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True)
    zip = models.PositiveIntegerField()
    gallery_photograph = models.CharField(max_length=200, blank=True, null=True)
    amount = models.CharField(max_length=11, blank=True, null=True)
    url_key = models.CharField(max_length=200, blank=True, null=True)
    is_featured = models.BooleanField(max_length=1, choices=[(0, 'NO'), (1, 'YES')],)
    user = models.ForeignKey('auth.User')
    
    class Meta:
        db_table = "events"
        
class EventsDataUrl(models.Model):
    url = models.CharField(max_length=200,)
    
    class Meta:
        db_table = "events_data_url"
        
class EventsUrl(models.Model):
    url = models.CharField(max_length=200,)
    
    class Meta:
        db_table = "events_url"
        
class EventCategories(models.Model):
    name = models.CharField(max_length=200,)
    url_key = models.CharField(max_length=200,)
    parent_id = models.PositiveIntegerField(blank=True, null=True)
    status = models.BooleanField(max_length=1, choices=[(0, 'inactive'), (1, 'active')], default="1",)
    added_by = models.ForeignKey('auth.User')
    added_on = models.DateTimeField(default=timezone.now, blank=True, null=True)
    
    class Meta:
        db_table = "event_categories"
        
class EventTypes(models.Model):
    name = models.CharField(max_length=200,)
    url_key = models.CharField(max_length=200,)
    parent_id = models.PositiveIntegerField(blank=True, null=True)
    status = models.BooleanField(max_length=1, choices=[(0, 'inactive'), (1, 'active')], default="1",)
    added_by = models.ForeignKey('auth.User')
    added_on = models.DateTimeField(default=timezone.now, blank=True, null=True)
    
    class Meta:
        db_table = "event_types"
        
class GenreCategories(models.Model):
    name = models.CharField(max_length=200,)
    url_key = models.CharField(max_length=200,)
    status = models.BooleanField(max_length=1, choices=[(0, 'inactive'), (1, 'active')], default="1",)
    added_by = models.ForeignKey('auth.User')
    added_on = models.DateTimeField(default=timezone.now, blank=True, null=True)
    
    class Meta:
        db_table = "genre_categories"
        
class MailTemplates(models.Model):
    mail_title = models.CharField(max_length=200,)
    field_name = models.CharField(max_length=200,)
    is_html = models.BooleanField(max_length=1, choices=[(0, 'NO'), (1, 'YES')], default="1",)
    from_email = models.CharField(max_length=200,)
    reply_to_email = models.CharField(max_length=200,)
    return_to_email = models.CharField(max_length=200,)
    smtp_username = models.CharField(max_length=50,)
    smtp_password = models.CharField(max_length=100,)
    smtp_host = models.CharField(max_length=50,)
    smtp_port = models.CharField(max_length=6,)
    mail_subject = models.CharField(max_length=200,)
    mail_content = models.TextField(blank=True, null=True,)
    mail_subject = models.BooleanField(max_length=1, choices=[(0, 'inactive'), (1, 'active')], default="1",)
    
    class Meta:
        db_table = "mail_templates"
        
class Media(models.Model):
    file_name = models.CharField(max_length=150,)
    author = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=150,)
    mime_type = models.CharField(max_length=200,)
    date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    
    class Meta:
        db_table = "media"
        
class Partners(models.Model):
    event = models.ForeignKey('Events')
    partners_name = models.CharField(max_length=150,)
    partners_description = models.TextField(blank=True)
    
    class Meta:
        db_table = "partners"
        
class Portfolio(models.Model):
    user = models.ForeignKey('auth.User')
    name_of_event = models.CharField(max_length=150,)
    pic_of_event = models.ForeignKey('media')
    des = models.TextField(blank=True,)
    date_of_event = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = "portfolio"
        
class PropertyTypes(models.Model):
    name = models.CharField(max_length=200,)
    url_key = models.CharField(max_length=200,)
    parent_id = models.PositiveIntegerField(blank=True, null=True)
    status = models.BooleanField(max_length=1, choices=[(0, 'inactive'), (1, 'active')], default="1",)
    added_by = models.ForeignKey('auth.User')
    added_on = models.DateTimeField(default=timezone.now, blank=True, null=True)
    
    class Meta:
        db_table = "property_types"
        
class Speaker(models.Model):
    event = models.ForeignKey('Events')
    speakers_name = models.CharField(max_length=200,)
    speaker_description = models.TextField(blank=True, null=True,)
        
    class Meta:
        db_table = "speaker"
        
class Sponsers(models.Model):
    event = models.ForeignKey('Events')
    sponsers_name = models.CharField(max_length=20,)
        
    class Meta:
        db_table = "sponsers"
        
class StaticPages(models.Model):
    title = models.CharField(max_length=250,)
    description = models.TextField(blank=True, null=True,)
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)
    update = models.DateTimeField(default=timezone.now, blank=True, null=True)
    status = models.BooleanField(max_length=1, choices=[(0, 'inactive'), (1, 'active')], default="1",)
    meta_title = models.CharField(max_length=150,)
    meta_description = models.CharField(max_length=250,)
    url_key = models.CharField(max_length=200,)
    
    class Meta:
        db_table = "static_pages"
        
class SysSettings(models.Model):
    title = models.CharField(max_length=200,)
    field_name = models.CharField(max_length=200, blank=True, null=True,)
    type = models.BooleanField(max_length=1, choices=[(0, 'text'), (1, 'textarea'), (2, 'select')], default="0",)
    select_items = models.TextField(blank=True, null=True,)
    value = models.TextField(blank=True, null=True,)
    is_required = models.BooleanField(max_length=1, choices=[(0, 'no'), (1, 'yes')], default="0",)
    is_core_config_item = models.BooleanField(max_length=1, choices=[(0, 'no'), (1, 'yes')], default="1",)
    created = models.DateTimeField(default=timezone.now, blank=True, null=True)
    status = models.BooleanField(max_length=1, choices=[(0, 'inactive'), (1, 'active')], default="1",)
    
    class Meta:
        db_table = "sys_settings"
        
class Tags(models.Model):
    blog = models.ForeignKey('Blogs')
    tags = models.CharField(max_length=200,)
    url_key = models.CharField(max_length=200, blank=True, null=True,)
    
    class Meta:
        db_table = "tags"
        
class TypesOfEvents(models.Model):
    event = models.ForeignKey('Events')
    event_types = models.ForeignKey('EventTypes')
    
    class Meta:
        db_table = "types_of_events"
        
class types_of_event_manager(models.Model):
    user = models.ForeignKey('auth.User')
    event_types = models.ForeignKey('EventTypes')
    
    class Meta:
        db_table = "types_of_event_manager"
        
class UserEmailVerification(models.Model):
    user = models.ForeignKey('auth.User')
    code = models.CharField(max_length=200,)
    status = models.BooleanField(max_length=1, choices=[(0, 'inactive'), (1, 'active')], default="1",)
    class Meta:
        db_table = "user_email_verification"
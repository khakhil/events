# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 10:34
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0002_auto_20170526_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesOfEventManagers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'categories_of_event_managers',
            },
        ),
        migrations.CreateModel(
            name='CategoriesOfEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'categories_of_events',
            },
        ),
        migrations.CreateModel(
            name='CiSessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(blank=True, max_length=200, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('data', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'ci_sessions',
            },
        ),
        migrations.CreateModel(
            name='ContactSubmissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message=b"Phone number must be entered in the format: '0 to 9'. Up to 10 digits allowed.", regex=b'^\\+?1?\\d{9,15}$')])),
                ('message', models.TextField(blank=True, null=True)),
                ('submit_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('subject', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'contact_submissions',
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sortname', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=200)),
                ('url_key', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='CurlEventUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'curl_event_url',
            },
        ),
        migrations.CreateModel(
            name='EmailNewsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'email_newsletter',
            },
        ),
        migrations.CreateModel(
            name='Enquiries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message=b"Phone number must be entered in the format: '0 to 9'. Up to 10 digits allowed.", regex=b'^\\+?1?\\d{9,15}$')])),
                ('message', models.TextField(blank=True, null=True)),
                ('rent_or_sale', models.CharField(choices=[(b'Rent', b'Rent'), (b'Sale', b'Sale')], max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('property_type', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=200)),
                ('price', models.FloatField(null=True)),
                ('zip', models.CharField(max_length=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('user_ip', models.CharField(max_length=100)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Countries')),
            ],
            options={
                'db_table': 'enquiries',
            },
        ),
        migrations.CreateModel(
            name='EventCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url_key', models.CharField(max_length=200)),
                ('parent_id', models.PositiveIntegerField(blank=True, null=True)),
                ('status', models.BooleanField(choices=[(0, b'inactive'), (1, b'active')], default=b'1', max_length=1)),
                ('added_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'event_categories',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('tag_line', models.CharField(max_length=200)),
                ('event_start_date', models.DateField(blank=True)),
                ('event_start_time', models.TimeField(blank=True)),
                ('event_end_date', models.DateField(blank=True)),
                ('event_end_time', models.TimeField(blank=True)),
                ('logo', models.PositiveIntegerField(blank=True, null=True)),
                ('banner_1_event', models.PositiveIntegerField(blank=True, null=True)),
                ('banner_2_event', models.PositiveIntegerField(blank=True, null=True)),
                ('banner_3_event', models.PositiveIntegerField(blank=True, null=True)),
                ('event_description', models.CharField(blank=True, max_length=200, null=True)),
                ('organizer', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line_1', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=200, null=True)),
                ('zip', models.PositiveIntegerField()),
                ('gallery_photograph', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.CharField(blank=True, max_length=11, null=True)),
                ('url_key', models.CharField(blank=True, max_length=200, null=True)),
                ('is_featured', models.BooleanField(choices=[(0, b'NO'), (1, b'YES')], max_length=1)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Countries')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='EventsDataUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'events_data_url',
            },
        ),
        migrations.CreateModel(
            name='EventsUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'events_url',
            },
        ),
        migrations.CreateModel(
            name='EventTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url_key', models.CharField(max_length=200)),
                ('parent_id', models.PositiveIntegerField(blank=True, null=True)),
                ('status', models.BooleanField(choices=[(0, b'inactive'), (1, b'active')], default=b'1', max_length=1)),
                ('added_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'event_types',
            },
        ),
        migrations.CreateModel(
            name='GenreCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url_key', models.CharField(max_length=200)),
                ('status', models.BooleanField(choices=[(0, b'inactive'), (1, b'active')], default=b'1', max_length=1)),
                ('added_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'genre_categories',
            },
        ),
        migrations.CreateModel(
            name='MailTemplates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_title', models.CharField(max_length=200)),
                ('field_name', models.CharField(max_length=200)),
                ('is_html', models.BooleanField(choices=[(0, b'NO'), (1, b'YES')], default=b'1', max_length=1)),
                ('from_email', models.CharField(max_length=200)),
                ('reply_to_email', models.CharField(max_length=200)),
                ('return_to_email', models.CharField(max_length=200)),
                ('smtp_username', models.CharField(max_length=50)),
                ('smtp_password', models.CharField(max_length=100)),
                ('smtp_host', models.CharField(max_length=50)),
                ('smtp_port', models.CharField(max_length=6)),
                ('mail_content', models.TextField(blank=True, null=True)),
                ('mail_subject', models.BooleanField(choices=[(0, b'inactive'), (1, b'active')], default=b'1', max_length=1)),
            ],
            options={
                'db_table': 'mail_templates',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=150)),
                ('author', models.PositiveIntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=150)),
                ('mime_type', models.CharField(max_length=200)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'db_table': 'media',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partners_name', models.CharField(max_length=150)),
                ('partners_description', models.TextField(blank=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Events')),
            ],
            options={
                'db_table': 'partners',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_event', models.CharField(max_length=150)),
                ('des', models.TextField(blank=True)),
                ('date_of_event', models.DateTimeField(blank=True, null=True)),
                ('pic_of_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'portfolio',
            },
        ),
        migrations.CreateModel(
            name='PropertyTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url_key', models.CharField(max_length=200)),
                ('parent_id', models.PositiveIntegerField(blank=True, null=True)),
                ('status', models.BooleanField(choices=[(0, b'inactive'), (1, b'active')], default=b'1', max_length=1)),
                ('added_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'property_types',
            },
        ),
        migrations.CreateModel(
            name='speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speakers_name', models.CharField(max_length=200)),
                ('speaker_description', models.TextField(blank=True, null=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Events')),
            ],
            options={
                'db_table': 'speaker',
            },
        ),
        migrations.CreateModel(
            name='Sponsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsers_name', models.CharField(max_length=20)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Events')),
            ],
            options={
                'db_table': 'sponsers',
            },
        ),
        migrations.CreateModel(
            name='StaticPages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('update', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('status', models.BooleanField(choices=[(0, b'inactive'), (1, b'active')], default=b'1', max_length=1)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_description', models.CharField(max_length=250)),
                ('url_key', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'static_pages',
            },
        ),
        migrations.CreateModel(
            name='SysSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('field_name', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.BooleanField(choices=[(0, b'text'), (1, b'textarea'), (2, b'select')], default=b'0', max_length=1)),
                ('select_items', models.TextField(blank=True, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('is_required', models.BooleanField(choices=[(0, b'no'), (1, b'yes')], default=b'0', max_length=1)),
                ('is_core_config_item', models.BooleanField(choices=[(0, b'no'), (1, b'yes')], default=b'1', max_length=1)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('status', models.BooleanField(choices=[(0, b'inactive'), (1, b'active')], default=b'1', max_length=1)),
            ],
            options={
                'db_table': 'sys_settings',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=200)),
                ('url_key', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='types_of_event_manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventTypes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'types_of_event_manager',
            },
        ),
        migrations.CreateModel(
            name='TypesOfEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Events')),
                ('event_types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventTypes')),
            ],
            options={
                'db_table': 'types_of_events',
            },
        ),
        migrations.CreateModel(
            name='UserEmailVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('status', models.BooleanField(choices=[(0, b'inactive'), (1, b'active')], default=b'1', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_email_verification',
            },
        ),
        migrations.AddField(
            model_name='blogs',
            name='unique_display',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='excerpt',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='post_type',
            field=models.CharField(blank=True, choices=[(b'', b''), (b'Blog', b'Blog'), (b'News', b'News')], default=b'Blog', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='status',
            field=models.CharField(blank=True, choices=[(b'', b''), (b'Draft', b'Draft'), (b'Trash', b'Trash'), (b'Published', b'Published')], default=b'Draft', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tags',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Blogs'),
        ),
        migrations.AddField(
            model_name='enquiries',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.PropertyTypes'),
        ),
        migrations.AddField(
            model_name='categoriesofevents',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Events'),
        ),
        migrations.AddField(
            model_name='categoriesofevents',
            name='event_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventCategories'),
        ),
        migrations.AddField(
            model_name='categoriesofeventmanagers',
            name='event_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventCategories'),
        ),
        migrations.AddField(
            model_name='categoriesofeventmanagers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogs',
            name='genre_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.GenreCategories'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='pic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Media'),
        ),
    ]

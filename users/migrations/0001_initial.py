# Generated by Django 4.0.5 on 2022-09-02 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('short_intro', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(max_length=40)),
                ('bio', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/')),
                ('social_github', models.CharField(blank=True, max_length=2000, null=True)),
                ('social_twitter', models.CharField(blank=True, max_length=2000, null=True)),
                ('social_lindin', models.CharField(blank=True, max_length=2000, null=True)),
                ('social_youtube', models.CharField(blank=True, max_length=2000, null=True)),
                ('social_website', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name=uuid.uuid4)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

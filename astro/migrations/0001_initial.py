# Generated by Django 4.2.4 on 2023-08-15 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(default='', max_length=20)),
                ('Second_Name', models.CharField(default='', max_length=20)),
                ('bio', models.TextField(blank=True)),
                ('code', models.CharField(blank=True, max_length=8)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(default='city', max_length=200)),
                ('Phone_Number', models.CharField(max_length=10, null=True)),
                ('image', models.ImageField(default='deafault.jpeg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
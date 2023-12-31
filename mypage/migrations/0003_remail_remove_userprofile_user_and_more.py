# Generated by Django 4.1 on 2023-08-16 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mypage', '0002_category_userprofile_userremail_delete_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remail1', models.EmailField(default='', max_length=255, null=True, unique=True)),
                ('remail2', models.EmailField(default='', max_length=255, null=True, unique=True)),
                ('remail3', models.EmailField(default='', max_length=255, null=True, unique=True)),
                ('remail4', models.EmailField(default='', max_length=255, null=True, unique=True)),
                ('remail5', models.EmailField(default='', max_length=255, null=True, unique=True)),
                ('category1', models.CharField(default='', max_length=10, null=True)),
                ('category2', models.CharField(default='', max_length=10, null=True)),
                ('category3', models.CharField(default='', max_length=10, null=True)),
                ('category4', models.CharField(default='', max_length=10, null=True)),
                ('category5', models.CharField(default='', max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userremail',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='UserRemail',
        ),
    ]

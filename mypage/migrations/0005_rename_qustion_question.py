# Generated by Django 4.1 on 2023-08-17 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0004_qustion_choice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Qustion',
            new_name='Question',
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-17 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='descrption',
            new_name='description',
        ),
    ]
# Generated by Django 3.2 on 2021-10-30 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211030_2001'),
    ]

    operations = [
        migrations.DeleteModel(
            name='employe',
        ),
        migrations.DeleteModel(
            name='schedule',
        ),
    ]

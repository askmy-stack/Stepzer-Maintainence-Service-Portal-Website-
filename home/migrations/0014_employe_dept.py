# Generated by Django 3.2 on 2021-10-30 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='dept',
            field=models.CharField(choices=[('cleaning', 'cleaning'), ('security', 'security')], default=None, max_length=20),
            preserve_default=False,
        ),
    ]

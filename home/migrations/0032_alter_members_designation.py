# Generated by Django 3.2 on 2021-11-20 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_alter_members_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='designation',
            field=models.CharField(default='', max_length=20),
        ),
    ]

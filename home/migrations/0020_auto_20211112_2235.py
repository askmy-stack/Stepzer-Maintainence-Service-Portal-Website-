# Generated by Django 3.2 on 2021-11-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_transactions_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='From_mon',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='To_mon',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='Year',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='path',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='status',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='timestamp',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transact_id',
            field=models.IntegerField(default=None, unique=True),
        ),
    ]

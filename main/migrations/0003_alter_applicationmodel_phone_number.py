# Generated by Django 4.0.4 on 2022-05-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_applicationmodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='phone_number',
            field=models.CharField(max_length=250),
        ),
    ]
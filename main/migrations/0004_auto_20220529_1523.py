# Generated by Django 3.2.1 on 2022-05-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_applicationmodel_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationmodel',
            name='email',
            field=models.CharField(default='email@email.com', max_length=200),
        ),
        migrations.AddField(
            model_name='applicationmodel',
            name='visited',
            field=models.BooleanField(default=False),
        ),
    ]

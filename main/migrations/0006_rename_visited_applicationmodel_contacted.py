# Generated by Django 3.2.1 on 2022-05-30 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_applicationmodel_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationmodel',
            old_name='visited',
            new_name='contacted',
        ),
    ]
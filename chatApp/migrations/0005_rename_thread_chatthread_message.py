# Generated by Django 3.2.5 on 2021-08-02 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0004_chatthread_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatthread',
            old_name='thread',
            new_name='message',
        ),
    ]

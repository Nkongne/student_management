# Generated by Django 3.1.4 on 2021-02-05 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report_card', '0007_remove_note_examen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Examen',
        ),
    ]

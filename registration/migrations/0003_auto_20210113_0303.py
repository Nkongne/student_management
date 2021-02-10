# Generated by Django 3.1.4 on 2021-01-13 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20201222_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.classe'),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.parent'),
        ),
    ]

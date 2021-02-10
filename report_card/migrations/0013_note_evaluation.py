# Generated by Django 3.1.4 on 2021-02-05 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report_card', '0012_evaluation'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='evaluation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='report_card.evaluation'),
            preserve_default=False,
        ),
    ]

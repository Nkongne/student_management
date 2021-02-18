# Generated by Django 3.1.4 on 2021-02-10 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report_card', '0018_examen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discipline',
            options={'ordering': ('intitule', 'coef')},
        ),
        migrations.AlterModelOptions(
            name='examen',
            options={'ordering': ('trimestre', 'annee')},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ('evaluation1', 'evaluation2')},
        ),
        migrations.AddField(
            model_name='note',
            name='examen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='report_card.examen'),
            preserve_default=False,
        ),
    ]
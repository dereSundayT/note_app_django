# Generated by Django 3.1 on 2020-08-04 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_note_background_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='background_color',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='note.colors'),
        ),
    ]

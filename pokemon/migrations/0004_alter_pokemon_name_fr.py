# Generated by Django 4.0.4 on 2022-10-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0003_rename_modified_at_pokemon_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name_fr',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]

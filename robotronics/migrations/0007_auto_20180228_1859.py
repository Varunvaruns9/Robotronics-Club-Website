# Generated by Django 2.0 on 2018-02-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotronics', '0006_auto_20180131_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(choices=[('Coord16', 'Coord16'), ('Coord', 'Coord'), ('Team', 'Team'), ('Team16', 'Team16'), ('Webdev', 'Webdev')], default='Team', max_length=20),
        ),
    ]
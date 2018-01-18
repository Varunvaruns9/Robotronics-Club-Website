# Generated by Django 2.0 on 2018-01-18 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Faculty', 'Faculty'), ('Coord', 'Coord'), ('Team', 'Team'), ('WebDev', 'WebDev')], default='Team', max_length=20)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
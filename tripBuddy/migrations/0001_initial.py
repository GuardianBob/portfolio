# Generated by Django 2.2.13 on 2021-04-20 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('details', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('joined_by', models.ManyToManyField(blank=True, related_name='extra_trips', to='loginApp.User')),
                ('planned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planned_trips', to='loginApp.User')),
            ],
        ),
    ]
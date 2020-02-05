# Generated by Django 2.2.5 on 2020-02-05 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercury', '0006_delete_simulateddata'),
    ]

    operations = [
        migrations.CreateModel(
            name='WindSpeedSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('current_windspeed', models.FloatField(default=0)),
            ],
        ),
    ]
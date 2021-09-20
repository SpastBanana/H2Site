# Generated by Django 3.1.7 on 2021-09-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehicleStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('vehicle_id', models.CharField(max_length=20)),
                ('laden', models.BooleanField()),
                ('error_g', models.BooleanField()),
                ('tanken', models.BooleanField()),
                ('baterij_temp', models.BooleanField()),
                ('batterij_span_laag', models.BooleanField()),
                ('batterij_span_hoog', models.BooleanField()),
                ('vermogen', models.FloatField()),
                ('batterij_percentage', models.FloatField()),
                ('actieradius', models.FloatField()),
                ('batterijspanning_minimum', models.FloatField()),
                ('batterijspanning_gemiddeld', models.FloatField()),
                ('batterijspanning_maximum', models.FloatField()),
                ('snelheid', models.FloatField()),
                ('airco_actief', models.FloatField()),
                ('error_12v', models.FloatField()),
                ('hoogspanningserror', models.FloatField()),
                ('motor_temperatuur_alarm', models.FloatField()),
                ('controller_temperatuur_alarm', models.FloatField()),
                ('airco_aan', models.FloatField()),
                ('motor_temperatuur', models.FloatField()),
                ('controller_temperatuur', models.FloatField()),
                ('spanning_12v', models.FloatField()),
                ('gemiddeld_verbruik', models.FloatField()),
                ('aantal_satellieten', models.FloatField()),
                ('batterij_temperatuur', models.FloatField()),
                ('kabine_temperatuur', models.FloatField()),
                ('kabine_ingestelde_temperatuur', models.FloatField()),
                ('olie_temperatuur', models.FloatField()),
                ('versnelling_x_richting', models.FloatField()),
                ('versnelling_y_richting', models.FloatField()),
                ('versnelling_z_richting', models.FloatField()),
                ('bedrijfstijd', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'vehicle statusses',
            },
        ),
    ]

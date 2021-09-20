from django.db import models


class vehicleStatus(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    vehicle_id = models.CharField(max_length=20)

    # CAN_ID 400
    laden = models.BooleanField()
    error_g = models.BooleanField()
    tanken = models.BooleanField()
    baterij_temp = models.BooleanField()
    batterij_span_laag = models.BooleanField()
    batterij_span_hoog = models.BooleanField()
    vermogen = models.FloatField()
    batterij_percentage = models.FloatField()
    actieradius = models.FloatField()
    batterijspanning_minimum = models.FloatField()
    batterijspanning_gemiddeld = models.FloatField()
    batterijspanning_maximum = models.FloatField()
    snelheid = models.FloatField()

    #CAN_ID 401
    airco_actief = models.FloatField()
    error_12v = models.FloatField()
    hoogspanningserror = models.FloatField()
    motor_temperatuur_alarm = models.FloatField()
    controller_temperatuur_alarm = models.FloatField()
    airco_aan = models.FloatField()
    motor_temperatuur = models.FloatField()
    controller_temperatuur = models.FloatField()
    spanning_12v = models.FloatField()
    gemiddeld_verbruik = models.FloatField()
    aantal_satellieten  = models.FloatField()
    batterij_temperatuur = models.FloatField()

    #CAN_ID 402
    kabine_temperatuur = models.FloatField()
    kabine_ingestelde_temperatuur = models.FloatField()
    olie_temperatuur = models.FloatField()
    versnelling_x_richting = models.FloatField()
    versnelling_y_richting = models.FloatField()
    versnelling_z_richting = models.FloatField()
    bedrijfstijd = models.FloatField()

    def __str__(self):
        return self.vehicle_id

    # def chartdata(self):
    #     return [
    #         self.laden,
    #         self.snelheid,
    #         self.trilling,
    #         self.vermogen,
    #         self.airco,
    #         self.verwarming,
    #         self.batterij_percentage,
    #         self.batterij_gemiddeld,
    #         self.batterij_temperatuur,
    #         self.motor_temperatuur,
    #         self.controller_temperatuur,
    #         self.actieradius,
    #         self.error
    #     ]

    class Meta:
        verbose_name_plural = "vehicle statusses"

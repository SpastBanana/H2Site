from django.db import models


class deltaStatus(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    meting_id = models.CharField(max_length=20)

    # Delta a
    TA1 = models.FloatField()
    TA2 = models.FloatField()
    TA1_2 = models.FloatField()

    # Delta b
    TB1 = models.FloatField()
    TB2 = models.FloatField()
    TB1_2 = models.FloatField()

    # Delta c
    TC1 = models.FloatField()
    TC2 = models.FloatField()
    TC1_2 = models.FloatField()

    # Delta d
    TD1 = models.FloatField()
    TD2 = models.FloatField()
    TD1_2 = models.FloatField()

    # flows
    flow_1 = models.FloatField()
    flow_2 = models.FloatField()
    flow_3 = models.FloatField()
    flow_H2 = models.FloatField()



    def __str__(self):
        return self.meting_id

    class Meta:
        verbose_name_plural = "delta en flow meting"

from django.db import models


class deltaStatus(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    meting_id = models.CharField(max_length=20)

    # Delta a Powercel
    TA1 = models.FloatField()
    TA2 = models.FloatField()
    TA1_2 = models.FloatField()
    TAP = models.FloatField()

    # Delta b Waterpomp
    TB1 = models.FloatField()
    TB2 = models.FloatField()
    TB1_2 = models.FloatField()
    TBP = models.FloatField()

    # Delta c Vloerverwarming (Vloer)
    TC1 = models.FloatField()
    TC2 = models.FloatField()
    TC1_2 = models.FloatField()
    TCP = models.FloatField()

    # Delta d reserve
    TD1 = models.FloatField()
    TD2 = models.FloatField()
    TD1_2 = models.FloatField()
    TDP = models.FloatField()

    # flows
    flow_1 = models.FloatField() #powercel
    flow_2 = models.FloatField() #Waterpomp
    flow_3 = models.FloatField() #Vloerverwarming
    flow_H2 = models.FloatField() #Waterstof

    #test
    test1 = models.FloatField()
    test2 = models.FloatField()
    test3 = models.FloatField()
    test4 = models.FloatField()



    def __str__(self):
        return self.meting_id

    class Meta:
        verbose_name_plural = "Metingen"
from django.db import models


class deltaStatus(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    meting_id = models.CharField(max_length=20)

    WP_IN = models.FloatField()
    WP_UIT = models.FloatField()
    delta_WP = models.FloatField()

    BC_ww_IN = models.FloatField()
    BC_ww_UIT = models.FloatField()
    delta_BC = models.FloatField()

    VloerVerw_IN = models.FloatField()
    VloerVerw_UIT = models.FloatField()
    delta_VloerVerw = models.FloatField()

    flow_WP = models.FloatField()
    flow_WW_BC = models.FloatField()
    flow_VloerVerw = models.FloatField()
    H2_massa_flow = models.FloatField()

    Temperatuur_hal = models.FloatField()
    Temperatuur_BC_uitlaat = models.FloatField()
    driewegklep_BC = models.FloatField()
    BC_intern_T1 = models.FloatField()

    driewegklep_WP = models.FloatField()
    geleverd_vermogen_therm = models.FloatField()
    opgenmoen_vermogen_el = models.FloatField()
    Accu_spanning = models.FloatField()
    Accu_stroom = models.FloatField()
    Accu_SOC = models.FloatField()


    def __str__(self):
            return self.meting_id

    class Meta:
        verbose_name_plural = "Metingen"
from rest_framework import generics, status
from rest_framework.views import APIView

from .models import vehicleStatus
from .serializers import viewVehicleStatusSerializer
from rest_framework.response import Response

class viewVehicleStatusses(generics.ListAPIView):
    serializer_class = viewVehicleStatusSerializer
    queryset = vehicleStatus.objects.all()

class createVehicleStatus(APIView):

    def post(self, request, format=None):
        try:
            #Decode Message
            payload_enc = request.data[1]["vs"]
            payload = bytes.fromhex(payload_enc).decode('utf-8')

            #Split message
            values = []
            for i in range(0, len(payload), 2):
                value_enc = payload[i:i + 2]
                value = int(value_enc, 16)
                values.append(value)

            alarm_enc = values[0]
            vermogen = values[1] -100
            batterij_percentage = values[2]
            actieradius = values[3] /10
            batterijspanning_minimum  = (values[4] +200) /100
            batterijspanning_gemiddeld  = (values[5] +200) /100
            batterijspanning_maximum  = (values[6] +200) /100
            snelheid = values[7]

            info_enc = values[8]
            motor_temperatuur = values[9] -100
            controller_temperatuur = values[10] -100
            spanning_12v = values[11] /10
            gemiddeld_verbruik = values[13] *10
            satelliet_enc = values[14]
            batterij_temperatuur = values[15] -100

            kabine_temperatuur = values[16] -100
            kabine_ingestelde_temperatuur = values[17] -100
            olie_temperatuur = values[18]
            versnelling_x_richting = values[19] /4
            versnelling_y_richting = values[20] /4
            versnelling_z_richting = values[21] /4
            bedrijfstijd_lowbyte = values[22]
            bedrijfstijd_highbyte = values[23]


            # decode alarm
            alarm = '{0:08b}'.format(int(alarm_enc))
            laden =  bool(alarm[0])
            error_g = bool(alarm[1])
            tanken = bool(alarm[2])
            baterij_temp = bool(alarm[4])
            batterij_span_laag = bool(alarm[5])
            batterij_span_hoog = bool(alarm[6])

            # decode info
            info = '{0:08b}'.format(int(info_enc))
            airco_actief = bool(info[1])
            error_12v = bool(info[2])
            hoogspanningserror = bool(info[3])
            motor_temperatuur_alarm = bool(info[5])
            controller_temperatuur_alarm = bool(info[6])
            airco_aan = bool(info[7])

            # decode satalliet
            satelliet = '{0:08b}'.format(int(satelliet_enc))
            aantal_satellieten = int(satelliet[0:7], 2)

            # decode bedrijfstijd
            bedrijfstijd_lowbyte = '{0:08b}'.format(int(bedrijfstijd_lowbyte))
            bedrijfstijd_highbyte = '{0:08b}'.format(int(bedrijfstijd_highbyte))
            bedrijfstijd = int(bedrijfstijd_highbyte + bedrijfstijd_lowbyte, 2)

            vehicle_id = request.headers.get('vehicleid').upper()
            vehicle_status = vehicleStatus(vehicle_id=vehicle_id, vermogen=vermogen, batterij_percentage=batterij_percentage, actieradius=actieradius,
                                           batterijspanning_minimum=batterijspanning_minimum, batterijspanning_gemiddeld=batterijspanning_gemiddeld,
                                           batterijspanning_maximum=batterijspanning_maximum, snelheid=snelheid,
                                           motor_temperatuur=motor_temperatuur, controller_temperatuur=controller_temperatuur,
                                           spanning_12v=spanning_12v, gemiddeld_verbruik=gemiddeld_verbruik,
                                           batterij_temperatuur=batterij_temperatuur, kabine_temperatuur=kabine_temperatuur,
                                           kabine_ingestelde_temperatuur=kabine_ingestelde_temperatuur, olie_temperatuur=olie_temperatuur,
                                           versnelling_x_richting=versnelling_x_richting, versnelling_y_richting=versnelling_y_richting,
                                           versnelling_z_richting=versnelling_z_richting, laden=laden,
                                           error_g=error_g, tanken=tanken, baterij_temp=baterij_temp, batterij_span_laag=batterij_span_laag,
                                           batterij_span_hoog=batterij_span_hoog, airco_actief=airco_actief, error_12v=error_12v,
                                           hoogspanningserror=hoogspanningserror, motor_temperatuur_alarm=motor_temperatuur_alarm,
                                           controller_temperatuur_alarm=controller_temperatuur_alarm, airco_aan=airco_aan,
                                           aantal_satellieten=aantal_satellieten, bedrijfstijd=bedrijfstijd,
                                           )
            vehicle_status.save()
            return Response({'Good request': 'saved'}, status=status.HTTP_200_OK)
        except:
            return Response({'Failed': 'bad request'}, status=status.HTTP_409_CONFLICT)



# class createVehicleStatus(APIView):
#
#     def post(self, request, format=None):
#         try:
#             payload = request.data[1]["vs"]
#
#             battery_perc = payload[2:4]
#             battery_perc = int(payload[2:3])-30
#
#             vehicle_id = request.headers.get('vehicle_id')
#             vehicle_status = vehicleStatus(vehicle_id=vehicle_id, payload=payload)
#             vehicle_status.save()
#             return Response({'Good request': 'saved'}, status=status.HTTP_201_CREATED)
#         except:
#             return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

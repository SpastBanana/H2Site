import traceback

from rest_framework import generics, status
from rest_framework.views import APIView

from .models import deltaStatus
from .serializers import viewDeltaStatusSerializer
from rest_framework.response import Response

class viewdeltaStatusses(generics.ListAPIView):
    serializer_class = viewDeltaStatusSerializer
    queryset = deltaStatus.objects.all()

class createdeltaStatus(APIView):

    def post(self, request, format=None):
        try:
            payload = request.data["payload"]
            print(payload, type(payload))

            payload = "".join(str(item) for item in payload).replace(".", "")

            values = []
            for i in range(0, len(payload), 4):
                value_enc = payload[i:i + 4]
                value = float("".join(value_enc))
                valueFloat = value / 100
                values.append(valueFloat)


            WP_IN = values[0]
            WP_UIT = values[1]
            delta_WP = values[2]

            BC_ww_IN = values[3]
            BC_ww_UIT = values[4]
            delta_BC = values[5]

            VloerVerw_IN = values[6]
            VloerVerw_UIT = values[7]
            delta_VloerVerw = values[8]

            flow_WP = values[9]
            flow_WW_BC = values[10]
            flow_VloerVerw = values[11]
            H2_massa_flow = values[12]

            Temperatuur_hal = values[13]
            Temperatuur_BC_uitlaat = values[14]
            driewegklep_BC = values[15]
            BC_intern_T1 = values[16]

            driewegklep_WP = values[17]
            geleverd_vermogen_therm = values[18]
            opgenmoen_vermogen_el = values[19]
            Accu_spanning = values[20]
            Accu_stroom = values[21]
            Accu_SOC = values[22]

            meting_id = request.headers.get('metingid').upper()
            delta_status = deltaStatus(meting_id=meting_id,
                                        WP_IN=WP_IN, WP_UIT=WP_UIT, delta_WP=delta_WP,
                                        BC_ww_IN=BC_ww_IN,BC_ww_UIT=BC_ww_UIT, delta_BC=delta_BC,
                                        VloerVerw_IN=VloerVerw_IN, VloerVerw_UIT=VloerVerw_UIT, delta_VloerVerw=delta_VloerVerw,
                                        flow_WP=flow_WP, flow_WW_BC=flow_WW_BC, flow_VloerVerw=flow_VloerVerw, H2_massa_flow=H2_massa_flow,
                                        Temperatuur_hal=Temperatuur_hal, Temperatuur_BC_uitlaat=Temperatuur_BC_uitlaat, driewegklep_BC=driewegklep_BC, BC_intern_T1=BC_intern_T1,

                                        driewegklep_WP=driewegklep_WP, geleverd_vermogen_therm=geleverd_vermogen_therm, opgenmoen_vermogen_el=opgenmoen_vermogen_el,
                                        Accu_spanning=Accu_spanning, Accu_stroom=Accu_stroom, Accu_SOC=Accu_SOC,
                                        )
            delta_status.save()
            return Response({'Good request': 'saved'}, status=status.HTTP_200_OK)
        except:
            return Response({'Failed': 'bad request', 'traceback': traceback.format_exc()}, status=status.HTTP_409_CONFLICT)



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
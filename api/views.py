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

            values = []
            for i in range(0, len(payload), 4):
                value_enc = payload[i:i + 4]
                value = float(value_enc)
                valueFloat = value / 100
                values.append(valueFloat)

            TA1 = values[0]
            TA2 = values[1]
            TB1 = values[2]
            TB2 = values[3]
            TC1 = values[4]
            TC2 = values[5]
            TD1 = values[6]
            TD2 = values[7]

            TA1_2 = values[8]
            TB1_2 = values[9]
            TC1_2 = values[10]
            TD1_2 = values[11]

            flow_1 = values[12]
            flow_2 = values[13]
            flow_3 = values[14]
            flow_H2 = values[15]

            TAP = values[16]
            TBP = values[17]
            TCP = values[18]
            TDP = values[19]

            meting_id = request.headers.get('metingid').upper()
            delta_status = deltaStatus(meting_id=meting_id,
                                        TA1=TA1, TA2=TA2, TA1_2=TA1_2,TAP=TAP,
                                        TB1=TB1, TB2=TB2, TB1_2=TB1_2, TBP=TBP,
                                        TC1=TC1, TC2=TC2, TC1_2=TC1_2, TCP=TCP,
                                        TD1=TD1, TD2=TD2, TD1_2=TD1_2, TDP=TDP,
                                        flow_1=flow_1, flow_2=flow_2, flow_3=flow_3, flow_H2=flow_H2,
                                        )
            delta_status.save()
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
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
            #Decode Message
            payload_enc = request.data[1]["ds"]
            payload = bytes.fromhex(payload_enc).decode('utf-8')

            #Split message
            values = []
            for i in range(0, len(payload), 2):
                value_enc = payload[i:i + 2]
                value = int(value_enc, 16)
                values.append(value)

            TA1 = values[0]
            TA2 = values[1]
            TA1_2 = values[2]
            TAP = values[3]

            TB1 = values[4]
            TB2 = values[5]
            TB1_2 = values[6]
            TBP = values[7]

            TC1 = values[8]
            TC2 = values[9]
            TC1_2 = values[10]
            TCP = values[11]

            TD1 = values[12]
            TD2 = values[13]
            TD1_2 = values[14]
            TDP = values[15]

            flow_1 = values[16]
            flow_2 = values[16]
            flow_3 = values[16]
            flow_H2 = values[16]


            # meting_id = request.headers.get('metingid').upper()
            delta_status = deltaStatus( #meting_id=meting_id,
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
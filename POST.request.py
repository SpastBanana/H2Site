from time import sleep
import requests

# API URL's
url_local = "http://84.104.232.125:8095/api/create-delta-status/"
url_cloud = "http://84.104.232.125:8095/api/create-delta-status/"

# API PAYLOAD's
payload_local = {
    "payload": waarde
    # "payload": "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
    }
payload_cloud = {
    "TA1":payload[0],
    "TA2":payload[1],
    "TA1_2":payload[2],
    "TAP":payload[3],

    "TB1":payload[4],
    "TB2":payload[5],
    "TB1_2":payload[6],
    "TBP":payload[7],

    "TC1":payload[8],
    "TC2":payload[9],
    "TC1_2":payload[10],
    "TCP":payload[11],

    "TD1":payload[12],
    "TD2":payload[13],
    "TD1_2":payload[14],
    "TDP":payload[15],

    "flow_1":payload[16],
    "flow_2":payload[17],
    "flow_3":payload[18],
    "flow_H2":payload[19]
    }

# API HEADER
header_local = {
    "metingid": "SYSTEM-1",
    }
header_cloud = {
    "header": "Metingen-Accenda",
    }

i = 0

while(i < 10):
    local = requests.post(url, data=payload, headers=header)
    cloud = requests.post(url_cloud, data=payload_cloud, headers=header_cloud
    sleep(1)
    print(i, p, waarde)
else:
    print("Done")

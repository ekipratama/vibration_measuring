

import time
import requests
import random
import SensorData as sd


prtg_host = '172.30.230.31'
prtg_host_port = '5050'
prtg_sensor_token = '5678'
interval = 0.5


def get_values():
    sensorValue = sd.read() * 100


    json_response = {
        "prtg": {
            "result": [
                {
                    "channel": "vibration",
                    "value": int(sensorValue)
                }
                
            ]
        }
    }
    return json_response


try:
    while True:
        try:
            json_response = get_values()
            # print output for debugging
            print(json_response)
            json_string = str(json_response)
            json_string = str.replace(json_string, '\'', '\"')
            prtg_request_URL = 'http://' + prtg_host + ':' + prtg_host_port + '/' + prtg_sensor_token + '?content=' + json_string
            print(prtg_request_URL)
            request = requests.get(prtg_request_URL)
            print(request.status_code)
        except:
            pass
        time.sleep(interval)

except KeyboardInterrupt:
    pass
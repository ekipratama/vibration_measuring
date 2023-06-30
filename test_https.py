

import time
import requests
import random


prtg_host = '172.30.230.31'
prtg_host_port = '5051'
prtg_sensor_token = '1234'
interval = 1


def get_values():
    randValue = random.randint(1, 10)


    json_response = {
        "prtg": {
            "result": [
                {
                    "channel": "vibration",
                    "value": randValue
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
import re

import bert
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
from bert_f import Precond, clie, psw
from requests import username


client_id = clie
server = "52.36.43.142"
ne_luboff = "192.168.88.34"
psw = psw


class Reconnect(mqtt.Client):
    server = "52.36.43.142"
    ne_luboff = "192.168.88.34"

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print('sending username')
            client.publish(topic="events/1//api/anon//", payload=bytearray(username), qos=2, retain=False)
            print('published')
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic)
        print(bert.decode(bytes(msg.payload)))

    def run(self):
        self.will_set(topic="version/4", payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=psw)
        self.connect(self.server, 1883, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()

        return rc


mqttc = Reconnect(client_id=client_id, clean_session=False)
rc = mqttc.run()

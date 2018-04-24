import re

import bert
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.

from erlastic import Atom
from requests import sms, login

global psw
global clie


class Precond(mqtt.Client):
    client_id = "reg_234BD084-5883-4E89-B86A-97305E903007"
    server = "52.36.43.142"
    ne_luboff = "192.168.88.34"

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Sending login request")
            client.publish(topic="events/1//api/anon//", payload=bytearray(login), qos=2, retain=False)
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic)
        print(bert.decode(bytes(msg.payload)))
        for node in (bert.decode(bytes(msg.payload))):
            if node == (Atom('ok'), Atom('sms_sent')):
                client.publish(topic="events/1//api/anon//", payload=bytearray(sms), qos=2, retain=False)
            elif re.findall(r"\(Atom\('ok2'\), Atom\('login'\)", str(node)):
                global psw
                global clie
                clie = str(node[2][0].decode("utf-8"))
                psw = str(node[2][1].decode("utf-8"))

                client.disconnect()

    def run(self):
        self.will_set(topic="version/4", payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=None)
        self.connect(self.server, 1883, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()

        return rc


mqttc = Precond(client_id=Precond.client_id, clean_session=False)
rc = mqttc.run()

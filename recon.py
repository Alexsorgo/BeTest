import re

import bert
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
from erlastic import Atom
from requests import sms, login, username

client_id = b'emqttd_234BD084-5883-4E89-B86A-97305E903007'
server = "52.36.43.142"
ne_luboff = "192.168.88.34"

def recon1():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            client.publish(topic="events/1//api/anon//", payload=bytearray(username), qos=2, retain=False)
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.


    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        print(msg.topic)
        print(bert.decode(bytes(msg.payload)))
        # for i in (bert.decode(bytes(msg.payload))):
            # print("string = " + str(i))
            # print(re.findall(r"\(Atom\('ok2'\), Atom\('login'\)",str(i)))
            #if i == (Atom('ok'), Atom('sms_sent')):
            #    client.publish(topic="events/1//api/anon//", payload=bytearray(sms), qos=2, retain=False)
            #elif re.findall(r"\(Atom\('ok2'\), Atom\('login'\)", str(i)):
            #    client_id = str(i[2][0])
            #    client.connect()
            #    client.publish(topic="events/1//api/anon//", payload=bytearray(username), qos=2, retain=False)


    client = mqtt.Client(client_id=client_id, clean_session=False)
    client.will_set(topic="version/4", payload=None, qos=2, retain=False)
    client.username_pw_set(username="api", password=b'd5b09942fcaa3d09420aa3f372b7925c19488f9d160808512067fafe5be6c80d8e412fe67af3de15a72e4172f40b47473bd2a4b3105a8e475c391d1c351990ede61c2058b81b4ab5d6c5deed27f741e1cd15d5feb2d4a77330237e9facd8eb6b')
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(ne_luboff, 1883, 60)

    client.loop_forever()

recon1()

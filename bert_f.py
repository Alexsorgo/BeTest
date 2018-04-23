import re

import os
import _thread

import bert
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.

from erlastic import Atom
from requests import sms, login

client_id = "reg_234BD084-5883-4E89-B86A-97305E903007"
server = "52.36.43.142"
ne_luboff = "192.168.88.34"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Sending login request")
        client.publish(topic="events/1//api/anon//", payload=bytearray(login), qos=2, retain=False)
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic)
    print(bert.decode(bytes(msg.payload)))
    for i in (bert.decode(bytes(msg.payload))):
        if i == (Atom('ok'), Atom('sms_sent')):
            client.publish(topic="events/1//api/anon//", payload=bytearray(sms), qos=2, retain=False)
        elif re.findall(r"\(Atom\('ok2'\), Atom\('login'\)", str(i)):
            clie = str(i[2][0])
            psw = str(i[2][1])
            print(clie)
            f = open("./recon.py", 'r')
            text = f.read()
            f.close()
            f = open("./recon.py", 'w')
            st = """client_id = 123"""
            # f.write(text.replace(st, "client_id = %s" % client_id).replace("password=None", "password=%s") % psw)
            f.write(text.replace(st, "client_id = %s" % clie).replace("password=None", "password=%s") % psw)
            f.close()
            client.disconnect()
            # _thread.start_new_thread(recon1(), ("Thread-1", 2,))
            os.system('python3 recon.py')


client = mqtt.Client(client_id=client_id, clean_session=False)
client.will_set(topic="version/4", payload=None, qos=2, retain=False)
client.username_pw_set(username="api", password=None)
client.on_connect = on_connect
client.on_message = on_message
client.connect(ne_luboff, 1883, 60)

# client.loop_start()
client.loop_forever()

import argparse
import json

import bert
import paho.mqtt.client as mqtt

import config
from models.number import login
from models.sms import sms


class Precodev(mqtt.Client):

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print('Send login \r\n')
            ''' Запрос на авторизацию '''
            if model == 'number':
                client.publish(topic="events/1//api/anon//", payload=bytearray(login()), qos=2,
                               retain=False)
            if model == 'sms':
                client.publish(topic="events/1//api/anon//", payload=bytearray(sms()), qos=2,
                               retain=False)

    def on_message(self, client, userdata, msg):
        # s = [i for i in msg.payload]
        # print('=' * 5 + 'RESPONSE' + '=' * 5 + '\r\n' + str(s) + '\r\n')
        print('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(bert.decode(bytes(msg.payload))) + '\r\n')
        client.disconnect()

    def run(self):
        self.will_set(topic="version/10", payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=None)
        # self.tls_set(tls_version=ssl.PROTOCOL_TLSv1)
        self.connect(config.server, 1883, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', dest='module', action='store',
                        choices=['number', 'sms'],
                        help='Special testing value')
    args = parser.parse_args()
    model = args.module
    my_number = config.my_number
    client_id = "reg_"+my_number
    mqtt = Precodev(client_id=client_id, clean_session=True)
    mqtt.run()

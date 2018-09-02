import re
import bert
import paho.mqtt.client as mqtt

from configs import config
from erlastic import Atom
from requests import login
from models import registration


class precond(mqtt.Client):
    client_id = "reg_234BD084-5883-4E89-B86A-97305E903007"
    server = config.SERVER
    ne_luboff = "192.168.88.34"
    clien = None
    pswd = None
    threadNumber = 0

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print('Send login \r\n')
            ''' Запрос на авторизацию '''
            client.publish(topic="events/1//api/anon//", payload=bytearray(login(self.my_number)), qos=2,
                           retain=False)

    def on_message(self, client, userdata, msg):
        # print("on_message")
        print('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(bert.decode(bytes(msg.payload))) + '\r\n')
        from models import registration
        registration.parser(client, msg.payload, self.my_number)
        for node in (bert.decode(bytes(msg.payload))):
            if re.findall(r"\(Atom\('ok2'\), Atom\('login'\)", str(node)):
                ''' Запись новых clien_id и password '''
                self.clien = str(node[2][0].decode("utf-8"))
                self.pswd = str(node[2][1].decode("utf-8"))
                client.disconnect()

    def run(self, my_number):
        self.my_number = my_number
        self.will_set(topic="version/8", payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=None)
        self.connect(self.server, 1883, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()

        return (self.clien, self.pswd)


class Reconnect(mqtt.Client):
    server = config.SERVER
    ne_luboff = "192.168.88.34"

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            ''' Запрос на изменение username '''
            # client.publish(topic="events/1//api/anon//", payload=bytearray(username), qos=2, retain=False)
            # print('published')
        # print("Connected with result code "+str(rc))

    def on_message(self, client, userdata, msg):
        # print(msg.topic)
        data = bert.decode(bytes(msg.payload))
        print('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(data) + '\r\n')
        registration.parser(client, msg.payload, self.my_number)
        if data[0] == Atom('Roster') and (data[-1]) == Atom('patch'):
            assert data[2] == b'first'+bytes(str(self.my_number).encode('utf-8'))
            client.disconnect()

    def run(self, my_number, pswa):
        self.firstname = 'first' + str(my_number)
        self.lastname = 'last' + str(my_number)
        self.my_number = my_number
        self.will_set(topic="version/8", payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=pswa)
        self.connect(self.server, 1883, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()

        return rc


def test_1():
    my_number = config.MY_NUMBER
    client_id = "reg_" + my_number
    mqtt = precond(client_id=client_id, clean_session=False)
    _, pswa = mqtt.run(my_number)
    client_id = "emqttd_" + my_number
    mqtt2 = Reconnect(client_id=client_id, clean_session=False)
    mqtt2.run(my_number, pswa)

# if __name__ == "__main__":
#     my_number = config.my_number
#     client_id = "reg_" + my_number
#     mqtt = TestC25412(client_id=client_id, clean_session=False)
#     _, pswa = mqtt.run(my_number)
#     client_id = "emqttd_" + my_number
#     mqtt2 = Reconnect(client_id=client_id, clean_session=False)
#     mqtt2.run(my_number, pswa)

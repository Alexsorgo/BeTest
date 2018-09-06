import bert
import paho.mqtt.client as mqtt

from configs import config
from erlastic import Atom
from tests.acceptance.base_test import Auth
from utils.logs import log

MAIN_NUMBER = config.CHINA_NUMBER
SERVER = config.SERVER
FRIEND_PHONE = config.JAPAN_NUMBER


class Logined(mqtt.Client):

    """User have ability to create group chat with avatar"""

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log.info("Reconnected successfully")

    def on_message(self, client, userdata, msg):
        # data = bert.decode(bytes(msg.payload))
        # log.info('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(data) + '\r\n')
        if data[0] == Atom("Profile"):
            for field in data:
                if field and list == type(field):
                    for room in field[0]:
                        if room and list == type(room) and room[0][0] == Atom('Room'):
                            print(room[-1])
            client.disconnect()
        # create_group_parser.parser(client, msg.payload, MAIN_NUMBER, FRIEND_PHONE, False, True)

    def run(self, pswa):
        self.will_set(topic="version/8", payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=pswa)
        self.connect(SERVER, 1883, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()

        return rc


def test_25453():
    client_id = "reg_" + MAIN_NUMBER
    mqtt_client = Auth(client_id=client_id, clean_session=False)
    _, pswa = mqtt_client.run(MAIN_NUMBER)
    client_id = "emqttd_" + MAIN_NUMBER
    mqtt2 = Logined(client_id=client_id, clean_session=False)
    mqtt2.run(pswa)

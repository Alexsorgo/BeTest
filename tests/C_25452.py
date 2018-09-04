import bert
import paho.mqtt.client as mqtt

from configs import config
from erlastic import Atom
from parsers import friend_by_phonebook_parser
from tests.base_test import Auth
from utils.logs import log

MAIN_NUMBER = config.CHINA_NUMBER
SERVER = config.SERVER
FRIEND_PHONE = config.UKRAINE_NUMBER


class Logined(mqtt.Client):

    """User have ability to search and send friend request to another user by phonebook"""

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log.info("Reconnected successfully \r\n")

    def on_message(self, client, userdata, msg):
        data = bert.decode(bytes(msg.payload))
        log.info('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(data) + '\r\n')
        friend_by_phonebook_parser.parser(client, msg.payload, MAIN_NUMBER, FRIEND_PHONE)

    def run(self, pswa):
        self.will_set(topic="version/8", payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=pswa)
        self.connect(SERVER, 1883, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()

        return rc


def test_25415():
    client_id = "reg_" + MAIN_NUMBER
    mqtt_client = Auth(client_id=client_id, clean_session=False)
    _, pswa = mqtt_client.run(MAIN_NUMBER)
    client_id = "emqttd_" + MAIN_NUMBER
    mqtt2 = Logined(client_id=client_id, clean_session=False)
    mqtt2.run(pswa)

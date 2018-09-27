import bert
import paho.mqtt.client as mqtt

from configs import config
from erlastic import Atom
from parsers import registration_parser, roster_update_parser
from tests.acceptance.base_test import Auth
from utils.convector import string_to_bytes
from utils.data_generation import magic
from utils.logs import log
from utils.verify import Verify

SERVER = config.SERVER
MAIN_NUMBER = config.CHINA_NUMBER
MAIN_FIRST_NAME = magic.get_word
MAIN_LAST_NAME = magic.get_word


class Logined(mqtt.Client):

    """User have ability to update first and last name"""

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log.info("Reconnected successfully")

    def on_message(self, client, userdata, msg):
        data = bert.decode(bytes(msg.payload))
        log.info('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(data) + '\r\n')
        roster_update_parser.parser(client, msg.payload, first_name=MAIN_FIRST_NAME, last_name=MAIN_LAST_NAME)

    def run(self, pswa):
        self.will_set(topic=config.PROTOCOL, payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=pswa)
        self.connect(SERVER, 1883, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()

        return rc


def test_25417():
    client_id = "reg_" + MAIN_NUMBER
    mqtt = Auth(client_id=client_id, clean_session=False)
    _, pswa = mqtt.run(MAIN_NUMBER)
    client_id = "emqttd_" + MAIN_NUMBER
    mqtt2 = Logined(client_id=client_id, clean_session=False)
    mqtt2.run(pswa)

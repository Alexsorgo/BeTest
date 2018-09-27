import bert
import paho.mqtt.client as mqtt

from configs import config
from erlastic import Atom
from parsers import friend_by_phone_parser
from tests.acceptance.base_test import Auth
from utils.convector import string_to_bytes
from utils.logs import log
from utils.verify import Verify

MAIN_NUMBER = config.CHINA_NUMBER
SERVER = config.SERVER
FRIEND_PHONE = config.JAPAN_NUMBER
FRIEND_FIRST_NAME = config.JAPAN_FIRSTNAME


class Logined(mqtt.Client):

    """User have ability to search and send friend request to another user by phone number"""

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log.info("Reconnected successfully")

    def on_message(self, client, userdata, msg):
        data = bert.decode(bytes(msg.payload))
        log.info('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(data) + '\r\n')
        friend_by_phone_parser.parser(client, msg.payload, MAIN_NUMBER, FRIEND_PHONE)
        if data[0] == Atom('Contact') and data[-1] == Atom('request'):
            log.info("Friend request send")
            Verify.true(data[0] == Atom('Contact') and data[-1] == Atom('request') and
                        data[1].split(b'_')[0] == string_to_bytes(FRIEND_PHONE), 'No request send')
            client.disconnect()
        if data == (Atom('io'), Atom('invalid_data'), b''):
            log.error("Request already send")
            client.disconnect()

    def run(self, pswa):
        self.will_set(topic=config.PROTOCOL, payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=pswa)
        self.connect(SERVER, 1883, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()

        return rc


def test_25413():
    client_id = "reg_" + MAIN_NUMBER
    mqtt_client = Auth(client_id=client_id, clean_session=False)
    _, pswa = mqtt_client.run(MAIN_NUMBER)
    client_id = "emqttd_" + MAIN_NUMBER
    mqtt2 = Logined(client_id=client_id, clean_session=False)
    mqtt2.run(pswa)

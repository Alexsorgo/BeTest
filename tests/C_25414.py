import bert
import paho.mqtt.client as mqtt

from configs import config
from erlastic import Atom
from parsers import friend_by_username_parser
from tests.base_test import Auth
from utils.convector import string_to_bytes
from utils.logs import log
from utils.verify import Verify

MAIN_NUMBER = config.CHINA_NUMBER
SERVER = config.SERVER
FRIEND_USERNAME = config.PERU_USERNAME


class Logined(mqtt.Client):

    """User have ability to search and send friend request to another user by username"""

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log.info("Reconnected successfully")

    def on_message(self, client, userdata, msg):
        data = bert.decode(bytes(msg.payload))
        # log.info('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(data) + '\r\n')
        friend_by_username_parser.parser(client, msg.payload, MAIN_NUMBER, FRIEND_USERNAME)
        if data[0] == Atom('Contact') and data[-1] == Atom('request'):
            log.info("Friend request send")
            print(data)
            Verify.true(data[0] == Atom('Contact') and data[-1] == Atom('request') and
                        data[5] == string_to_bytes(FRIEND_USERNAME), 'No request send')
            client.disconnect()
        if data == (Atom('io'), Atom('invalid_data'), b''):
            log.error("Request already send")
            client.disconnect()

    def run(self, pswa):
        self.will_set(topic="version/8", payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=pswa)
        self.connect(SERVER, 1883, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()

        return rc


def test_25414():
    client_id = "reg_" + MAIN_NUMBER
    mqtt_client = Auth(client_id=client_id, clean_session=False)
    _, pswa = mqtt_client.run(MAIN_NUMBER)
    client_id = "emqttd_" + MAIN_NUMBER
    mqtt2 = Logined(client_id=client_id, clean_session=False)
    mqtt2.run(pswa)

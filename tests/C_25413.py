import bert
import paho.mqtt.client as mqtt

from configs import config
from erlastic import Atom
from parsers import search, friend_invite
from tests.base_test import Auth
from utils.logs import log
from utils.verify import Verify

MAIN_NUMBER = config.CHINA_NUMBER
SERVER = config.SERVER
FRIEND_PHONE = config.AMERICA_NUMBER
FRIEND_FIRST_NAME = config.AMERICA_FIRSTNAME


class Logined(mqtt.Client):

    """User have ability to search another user by phone number"""

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log.info("Reconnected successfully \r\n")

    def on_message(self, client, userdata, msg):
        data = bert.decode(bytes(msg.payload))
        log.info('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(data) + '\r\n')
        friend_invite.parser(client, msg.payload, MAIN_NUMBER, FRIEND_PHONE)
        if data[0] == Atom('Contact') and data[-1] == Atom('request'):
            log.info("Verify contact found")
            log.debug(data)
            client.disconnect()

    def run(self, pswa):
        self.will_set(topic="version/8", payload=None, qos=2, retain=False)
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

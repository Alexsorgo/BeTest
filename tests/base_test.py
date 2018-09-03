import re
import bert

import paho.mqtt.client as mqtt
from configs import config
from erlastic import Atom
from models.number import login
from models.sms import sms
from utils.logs import log


class Auth(mqtt.Client):
    server = config.SERVER
    clien = None
    pswd = None
    threadNumber = 0

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log.info('Send login \r\n')
            client.publish(topic="events/1//api/anon//", payload=bytearray(login(self.my_number)), qos=2,
                           retain=False)

    def on_message(self, client, userdata, msg):
        log.info('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(bert.decode(bytes(msg.payload))) + '\r\n')
        for node in (bert.decode(bytes(msg.payload))):
            if node == (Atom('ok'), Atom('sms_sent')):
                client.publish(topic="events/1//api/anon//", payload=bytearray(sms(self.my_number)), qos=2,
                               retain=False)
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


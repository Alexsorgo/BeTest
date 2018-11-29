import argparse
import time

import bert
import paho.mqtt.client as mqtt

from erlastic import Atom

import config
from models.accept_friend import accept_friend
from models.ban_user import ban_user
from models.create_group import create_group
from models.get_profile import get_profile
from models.history import history_schedule, history_p2p
from models.ignore_request import ignore_request
from models.invite_friend import invite_friend
from models.delete import delete_user
from models.search_by_phone import search_by_phone
from models.search_by_username import search_by_username
from models.send_msg import send_message
from models.unban_user import unban_user
from models.update_name import update_name
from models.update_username import update_username


class Reconnect(mqtt.Client):

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            # print('sending username')
            ''' Запрос на изменение username '''
            if model == 'delete':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    delete_user(self.threadNumber)), qos=2, retain=False)
            if model == 'search':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    search_by_phone()), qos=2, retain=False)
            if model == 'search_username':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    search_by_username()), qos=2, retain=False)
            if model == 'invite_friend':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    invite_friend()), qos=2, retain=False)
            if model == 'name':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    update_name()), qos=2, retain=False)
            if model == 'username':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    update_username()), qos=2, retain=False)
            if model == 'history_schedule':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    history_schedule()), qos=2, retain=False)
            if model == 'history_p2p':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    history_p2p()), qos=2, retain=False)
            if model == 'accept_friend':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    accept_friend()), qos=2, retain=False)
            if model == 'send_message':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    send_message()), qos=2, retain=False)
            if model == 'create_group':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    create_group()), qos=2, retain=False)
            if model == 'ban_user':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    ban_user()), qos=2, retain=False)
            if model == 'unban_user':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    unban_user()), qos=2, retain=False)
            if model == 'ignore':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    ignore_request()), qos=2, retain=False)
            if model == 'get_profile':
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    get_profile()), qos=2, retain=False)

    def on_message(self, client, userdata, msg):
        # print(msg.topic)
        if bert.decode(bytes(msg.payload))[0] == Atom('Profile'):
            print('=' * 5 + 'PROFILE' + '=' * 5 + '\r\n' + str(bert.decode(bytes(msg.payload))) + '\r\n')
        # elif bert.decode(bytes(msg.payload))[1] == (Atom('ok'), b'phone'):
        #     print('response: '+ str(time.time()).split('.')[0])
        #     client.publish(topic="events/1//api/anon//", payload=bytearray(
        #         search_by_phone()), qos=2, retain=False)
        else:
            print('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(bert.decode(bytes(msg.payload))) + '\r\n')
            # client.disconnect()

    def run(self, threadNumber):
        pswa = config.password
        self.threadNumber = threadNumber
        self.will_set(topic="version/10", payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=pswa)
        self.connect(config.server, 1883, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()

        return rc


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', dest='module', action='store',
                        choices=['delete', 'search', 'invite_friend', 'name', 'username', 'history_schedule',
                                 'accept_friend', 'send_message', 'history_p2p', 'create_group', 'ignore', 'ban_user',
                                 'unban_user','get_profile','search_username'],
                        help='Special testing value')
    args = parser.parse_args()
    model = args.module
    number = config.my_number
    client_id = "emqttd_" + number
    mqtt = Reconnect(client_id=client_id, clean_session=False)
    mqtt.run(number)

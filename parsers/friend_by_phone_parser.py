import bert
from erlastic import Atom
from models.invite_friend import invite_friend
from models.search_by_phone import search_by_phone
from utils.logs import log

global user_id


def parser(client, payload, main_number, friend_phone):
    data = bert.decode(bytes(payload))

    for node in data:
        if node == Atom('Profile') and data[8] == 'init':
            roas = (bert.decode(bytes(payload))[3])
            global user_id
            user_id = roas[0][1]
            client.publish(topic="events/1//api/anon//", payload=bytearray(
                search_by_phone(user_id, friend_phone)), qos=2, retain=False)

        if node == Atom('io') and data[1] == (Atom('ok'), b'phone'):
            if data[2][6]:
                friend = data[2][6][0][1]
                my = main_number + '_' + str(user_id)
                log.debug("Add user {} \r\n".format(str(friend)))
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    invite_friend(my, friend)), qos=2, retain=False)
            if not data[2][6]:
                log.debug('Contact not found')
                client.disconnect()


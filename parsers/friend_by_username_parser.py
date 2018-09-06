import bert
from erlastic import Atom
from models.invite_friend import invite_friend
from models.search_by_username import search_by_username
from utils.logs import log

global user_id


def parser(client, payload, main_number, friend_username):
    data = bert.decode(bytes(payload))

    for node in data:
        if node == Atom('Profile') and data[8] == 'init':
            roas = (bert.decode(bytes(payload))[3])
            global user_id
            user_id = roas[0][1]
            client.publish(topic="events/1//api/anon//", payload=bytearray(
                search_by_username(user_id, friend_username)), qos=2, retain=False)

        if node == Atom('io') and data[1] == (Atom('ok'), b'username'):
            if data[2][6]:
                friend = data[2][6][0][1]
                my = main_number + '_' + str(user_id)
                log.debug("Add user {}".format(str(friend)))
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    invite_friend(my, friend)), qos=2, retain=False)
            if not data[2][6]:
                log.debug('Contact not found')
                client.disconnect()

import bert
from erlastic import Atom
from models.invite_friend import friend
from models.search_by_phone import search
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
                search(user_id=user_id, ref='phone', field='phone', type_r=Atom('=='), value=[friend_phone],
                       status=Atom('contact'))), qos=2, retain=False)

        if node == Atom('io') and data[1] == (Atom('ok'), b'phone'):
            if data[2][6]:
                friend = data[2][6][0][1]
                my = main_number + '_' + str(user_id)
                log.debug("Add user {} \r\n".format(str(friend)))
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    friend(my_id=my, friend_id=friend, status=Atom('request'))), qos=2, retain=False)
            if not data[2][6]:
                log.debug('Contact not found')
                log.debug(data)
                client.disconnect()


import bert
from erlastic import Atom
from models.friend_model import friend
from models.search_model import search
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
                search(user_id=user_id, ref='username', field='nick', type_r=Atom('=='), value=[friend_username],
                       status=Atom('contact'))), qos=2, retain=False)

        if node == Atom('io') and data[1] == (Atom('ok'), b'username'):
            if data[2][6]:
                friend_id = data[2][6][0][1]
                my = main_number + '_' + str(user_id)
                log.debug("Add user {}".format(str(friend_id)))
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    friend(my_id=my, friend_id=friend_id, status=Atom('request'))), qos=2, retain=False)
            if not data[2][6]:
                log.debug('Contact not found')
                client.disconnect()

    if data == (Atom('io'), (Atom('error'), Atom('invalid_data')), b''):
        log.error("Something going wrong")
        client.disconnect()

    if data == (Atom('io'), (Atom('error'), Atom('permission_denied')), b''):
        log.error("Something going wrong")
        client.disconnect()

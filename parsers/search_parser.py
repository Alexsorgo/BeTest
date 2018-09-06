import bert
from erlastic import Atom
from models.search_by_phone import search_by_phone


def parser(client, payload, number, friend_phone):
    data = bert.decode(bytes(payload))

    for node in data:

        if node == Atom('Profile') and data[8] == 'init':
            roas = (bert.decode(bytes(payload))[3])
            user_id = roas[0][1]
            client.publish(topic="events/1//api/anon//", payload=bytearray(
                search_by_phone(user_id, friend_phone)), qos=2, retain=False)
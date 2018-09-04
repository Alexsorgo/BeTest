import bert
from erlastic import Atom
from models.update_name import update_name


def parser(client, payload, first_name, last_name):
    data = bert.decode(bytes(payload))

    for node in data:

        if node == Atom('Profile') and (data[-1]) == Atom('init'):
            roas = (bert.decode(bytes(payload))[3])
            userid = roas[0][1]
            client.publish(topic="events/1//api/anon//", payload=bytearray(
                update_name(userid, first_name, last_name)), qos=2, retain=False)

import bert
from erlastic import Atom
from models.accept_friend import accept_friend


def parser(client, payload, main_number):
    data = bert.decode(bytes(payload))

    for node in data:
        if node == Atom('Profile') and data[8] == 'init':
            roster = (bert.decode(bytes(payload))[3])
            user_id = roster[0][1]
            my = main_number + '_' + str(user_id)
            contacts = data[3][0][6]
            for field in contacts:
                if field[0] == Atom('Contact') and field[-1] == Atom('authorization'):
                    client.publish(topic="events/1//api/anon//", payload=bytearray(
                        accept_friend(my, field[1])), qos=2, retain=False)

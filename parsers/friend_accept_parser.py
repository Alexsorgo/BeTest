import bert
from erlastic import Atom
from models.invite_friend import friend


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
                        friend(my_id=my, friend_id=field[1], status=Atom('confirm'))), qos=2, retain=False)

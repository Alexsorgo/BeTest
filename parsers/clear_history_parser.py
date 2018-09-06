import bert
from erlastic import Atom
from models.create_group import create_group
from models.history import history_group
from utils.convector import string_to_bytes
from utils.logs import log
from utils.verify import Verify

global user_id
global room_id


def parser(client, payload, main_number):
    data = bert.decode(bytes(payload))

    if data[0] == Atom("Profile"):
        contacts = data[3][0][6]
        for field in contacts:
            if field[0] == Atom('Contact') and field[1].split(b'_')[0] == string_to_bytes(main_number):
                log.debug('Main profile found')
                global user_id
                user_id = field[1]
                print(user_id)
        for field in data:
            if field and list == type(field):
                for room in field[0]:
                    if room and list == type(room) and room[0][0] == Atom('Room'):
                        global room_id
                        room_id = room[-1][1]
                        print(room_id)
        client.publish(topic="events/1//api/anon//", payload=bytearray(
            history_group(user_id, room_id)), qos=2,
                       retain=False)

    if data[0] == Atom('Message') and data[-1] == Atom('clear'):
        for field in data:
            if field and list == type(field) and tuple == type(field[0]):
                Verify.equals(b'History was removed', field[0][3], 'No history removed')
        client.disconnect()

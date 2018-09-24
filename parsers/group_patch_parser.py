import bert
from erlastic import Atom
from models.patch_group import patch_group
from utils.convector import string_to_bytes
from utils.logs import log
from utils.verify import Verify

global room_id
global my_alias


def parser(client, payload, room_name):
    data = bert.decode(bytes(payload))

    if data[0] == Atom("Profile"):
        for field in data:
            if field and list == type(field):
                for room in field[0]:
                    if room and list == type(room) and room[0][0] == Atom('Room'):
                        global room_id
                        room_id = room[-1][1]

        global my_alias
        my_alias = data[3][0][4] if data[3][0][4] else data[3][0][2]+data[3][0][3]
        client.publish(topic="events/1//api/anon//", payload=bytearray(
            patch_group(room_id, room_name)), qos=2,
                       retain=False)

    if data[0] == Atom('Message'):
        log.debug('Verify group patched')
        for field in data:
            if field and list == type(field) and tuple == type(field[0]):
                print(field[0][3])
                Verify.equals(b'Group is renamed to "'+string_to_bytes(room_name)+b'"', field[0][3], 'No message about patch')
        client.disconnect()

import bert
from erlastic import Atom
from models.create_group import create_group
from utils.convector import string_to_bytes
from utils.logs import log


def parser(client, payload, main_number, friend_phone):
    data = bert.decode(bytes(payload))

    for node in data:
        if node == Atom('Profile') and data[8] == 'init':
            contacts = data[3][0][6]
            for field in contacts:
                if field[0] == Atom('Contact') and field[1].split(b'_')[0] == string_to_bytes(main_number):
                    log.debug('My profile found')
                    main_id = field[1]
                    main_first_name = field[3]
                    main_last_name = field[4]
                    main_alias = []
                    if field[5]:
                        main_alias = field[5]
                if field[0] == Atom('Contact') and field[-1] == Atom('friend') and\
                        field[1].split(b'_')[0] == string_to_bytes(friend_phone):
                    friend_id = field[1]
                    friend_first_name = field[3]
                    friend_last_name = field[4]
                    friend_alias = []
                    if field[5]:
                        friend_alias = field[5]

            client.publish(topic="events/1//api/anon//", payload=bytearray(
                create_group(main_id, main_first_name, main_last_name, main_alias,
                             friend_id, friend_first_name, friend_last_name, friend_alias)), qos=2, retain=False)


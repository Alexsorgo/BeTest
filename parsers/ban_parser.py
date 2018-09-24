import bert
from enums import enums
from erlastic import Atom
from models.friend_model import friend
from utils.convector import string_to_bytes
from utils.logs import log


def parser(client, payload, main_number, friend_number, status):
    data = bert.decode(bytes(payload))
    global main_id
    global friend_id

    if status == enums.FRIEND_BAN:
        if data[0] == Atom("Profile"):
            for field in data[3][0][6]:
                if field[-1] == Atom('friend'):
                    if field[1].split(b'_')[0] == string_to_bytes(main_number):
                        log.debug('Main profile found')
                        main_id = field[1]
                    if field[0] == Atom('Contact') and field[1].split(b'_')[0] == string_to_bytes(friend_number):
                        friend_id = field[1]

            client.publish(topic="events/1//api/anon//", payload=bytearray(
                friend(my_id=main_id, friend_id=friend_id, status=Atom(status))), qos=2, retain=False)

        if data[0] == Atom("Contact") and data[-1] == Atom('banned'):
            log.debug('Contact banned')
            client.disconnect()

    if status == enums.FRIEND_UNBAN:
        if data[0] == Atom("Profile"):
            for field in data[3][0][6]:
                if field[-1] == Atom('friend'):
                    if field[1].split(b'_')[0] == string_to_bytes(main_number):
                        log.debug('Main profile found')
                        main_id = field[1]
                if field[-1] == Atom('banned'):
                    friend_id = field[1]

            client.publish(topic="events/1//api/anon//", payload=bytearray(
                friend(my_id=main_id, friend_id=friend_id, status=Atom(status))), qos=2, retain=False)

        if data[0] == Atom("Contact") and data[-1] == Atom('friend'):
            log.debug('Contact Unbanned')
            client.disconnect()

    if data == (Atom('io'), (Atom('error'), Atom('invalid_data')), b''):
        log.error("Something going wrong")
        client.disconnect()

    if data == (Atom('io'), (Atom('error'), Atom('permission_denied')), b''):
        log.error("Something going wrong")
        client.disconnect()

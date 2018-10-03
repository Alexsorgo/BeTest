import bert
from erlastic import Atom
from models.send_msg import send_message
from utils.convector import string_to_bytes
from utils.exception import InvalidData, PermissionDenied
from utils.logs import log
from utils.verify import Verify


def parser(chat_type, client, payload, main_number, friend_number, mime, message_type=None):
    data = bert.decode(bytes(payload))
    global main_id
    global friend_id
    global chat
    global message_id
    global member_id

    if data[0] == Atom("Profile"):
        if chat_type == 'p2p':
            for field in data[3][0][6]:
                if field[-1] == Atom('friend'):
                    if field[1].split(b'_')[0] == string_to_bytes(main_number):
                        log.debug('Main profile found')
                        main_id = field[1]
                    if field[0] == Atom('Contact') and field[-1] == Atom('friend') and \
                            field[1].split(b'_')[0] == string_to_bytes(friend_number):
                        friend_id = field[1]
                        if field[8]:
                            chat = field[8][3]
                            message_id = field[8][1]

            member_id = main_id

            if message_type in ['delete for all', 'delete for me']:
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    send_message(main_id, friend_id, chat, mime, message_id, message_type=None)), qos=2, retain=False)

            else:
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    send_message(main_id, friend_id, chat, mime, message_id, message_type, member_id)), qos=2,
                               retain=False)

        if chat_type == 'group':
            for field in data[3][0][6]:
                if field[-1] == Atom('friend'):
                    if field[1].split(b'_')[0] == string_to_bytes(main_number):
                        log.debug('Main profile found')
                        main_id = field[1]

            message_id = data[3][0][7][-1][15][1]
            chat = data[3][0][7][-1][7][0][3]
            friend_id = data[3][0][7][-1][1]
            member_id = data[3][0][7][-1][7][0][1]

            if message_type in ['delete for all', 'delete for me']:
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    send_message(main_id, friend_id, chat, mime, message_id, message_type=None)), qos=2, retain=False)

            else:
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    send_message(main_id, friend_id, chat, mime, message_id, message_type, member_id)), qos=2,
                               retain=False)

    if data[0] == Atom('Message') and message_type in ['delete for all', 'delete for me'] and data[-1] == []:
        message_id = data[1]
        client.publish(topic="events/1//api/anon//", payload=bytearray(
            send_message(main_id, friend_id, chat, mime, message_id, message_type, member_id)), qos=2,
                       retain=False)

    elif data[0] == Atom('Message') and data[-1] == Atom('delete'):
        log.debug('Verify group patched')
        Verify.true(data[1], "No message ID")
        client.disconnect()

    elif data[0] == Atom('Message'):
        log.debug('Verify group patched')
        Verify.true(data[1], "No message ID")
        client.disconnect()

    elif data == (Atom('io'), (Atom('error'), Atom('invalid_data')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise InvalidData("Invalid data response")

    if data == (Atom('io'), (Atom('error'), Atom('permission_denied')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise PermissionDenied("No permission")

import bert
from erlastic import Atom
from models.message_model import message_model
from models.p2p_model import p2p
from models.send_msg import send_message
from utils.convector import string_to_bytes
from utils.exception import InvalidData, PermissionDenied
from utils.logs import log
from utils.verify import Verify


def parser(client, payload, main_number, mime, message_type=None):
    data = bert.decode(bytes(payload))
    global main_id
    global friend_id
    global chat
    global message_id

    if data[0] == Atom("Profile"):
        for field in data[3][0][6]:
            if field[-1] == Atom('friend'):
                if field[1].split(b'_')[0] == string_to_bytes(main_number):
                    log.debug('Main profile found')
                    main_id = field[1]
                    friend_id = field[1]
                    chat = p2p(from_user=main_id, to=main_id)

        client.publish(topic="events/1//api/anon//", payload=bytearray(
            message_model(mime, container=Atom('chain'), feed_id=chat, from_user=main_id, to=main_id)), qos=2,
                       retain=False)

    if data[0] == Atom('Message') and message_type == 'delete for me' and data[-1] == []:
        message_id = data[1]
        client.publish(topic="events/1//api/anon//", payload=bytearray(
            send_message(main_id, friend_id, chat, mime, message_id, message_type, main_id)), qos=2,
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

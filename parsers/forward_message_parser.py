import bert
from erlastic import Atom
from models.job import job, act
from models.send_msg import send_message
from utils.convector import string_to_bytes
from utils.logs import log
from utils.verify import Verify


def parser(chat_type, client, payload, main_number, friend_number, mime, message_type=None):
    data = bert.decode(bytes(payload))
    global main_id
    global friend_id
    global p2p_chat
    global group_chat
    global message_id
    global member_id
    global group_friend_id

    if data[0] == Atom("Profile"):
        for field in data[3][0][6]:
            if field[-1] == Atom('friend'):
                if field[8]:
                    p2p_chat = field[8][3]

        group_chat = data[3][0][7][-1][6][0][3]
        group_friend_id = data[3][0][7][-1][1]

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
                        message_id = field[8][1]

            client.publish(topic="events/1//api/anon//", payload=bytearray(
                send_message(main_id, friend_id, p2p_chat, mime, message_id, message_type)), qos=2, retain=False)

        if chat_type == 'group':
            for field in data[3][0][6]:
                if field[-1] == Atom('friend'):
                    if field[1].split(b'_')[0] == string_to_bytes(main_number):
                        log.debug('Main profile found')
                        main_id = field[1]

            message_id = data[3][0][7][-1][15][1]
            friend_id = data[3][0][7][-1][1]
            member_id = data[3][0][7][-1][6][0][1]

            if message_type in ['delete for all', 'delete for me']:
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    send_message(main_id, friend_id, group_chat, mime, message_id, message_type=None)), qos=2,
                               retain=False)

            else:
                client.publish(topic="events/1//api/anon//", payload=bytearray(
                    send_message(main_id, friend_id, group_chat, mime, message_id, message_type, member_id)), qos=2,
                               retain=False)

    elif data[0] == Atom('Message') and data[11] == [Atom('forward')]:
        log.debug('Verify')
        log.debug(data)
        client.disconnect()

    elif data[0] == Atom('Message'):
        log.debug('Send job')
        message_model = []
        if chat_type == 'p2p':
            message_model = bert.decode(send_message(main_id, group_friend_id, group_chat, mime, data[1],
                                                     message_type='forward'))
        elif chat_type == 'group':
            message_model = bert.decode(send_message(main_id, friend_id, p2p_chat, mime, data[1],
                                                     message_type='forward'))
        act_model = act(name='publish', data=main_id)
        client.publish(topic="events/1//api/anon//", payload=bytearray(
            job(feed_id=act_model, data=[message_model], status=Atom('init'))), qos=2, retain=False)

    elif data == (Atom('io'), (Atom('error'), Atom('invalid_data')), b''):
        log.error("Something going wrong")
        client.disconnect()

    if data == (Atom('io'), (Atom('error'), Atom('permission_denied')), b''):
        log.error("Something going wrong")
        client.disconnect()

import time

import bert
from erlastic import Atom
from models.create_group import create_group
from models.member import member
from models.room_model import room
from utils.convector import string_to_bytes
from utils.exception import InvalidData, PermissionDenied
from utils.logs import log
from utils.verify import Verify


def parser(client, payload, name, main_number, friend_phone, avatar=False, alias_check=False, group_avatar=None):
    data = bert.decode(bytes(payload))
    global user_id
    global main_id
    global main_first_name
    global main_last_name
    global main_alias
    global friend_id
    global friend_first_name
    global friend_last_name
    global friend_alias

    if data[0] == Atom('Profile') and data[8] == 'init':
        contacts = data[3][0][6]
        for field in contacts:
            if field[0] == Atom('Contact') and field[1].split(b'_')[0] == string_to_bytes(main_number):
                log.debug('Main profile found')
                user_id = main_id = field[1]
                main_first_name = field[3]
                main_last_name = field[4]
                main_alias = []
                if field[5]:
                    main_alias = field[5]
            if field[0] == Atom('Contact') and field[-1] == Atom('friend') and \
                    field[1].split(b'_')[0] == string_to_bytes(friend_phone):
                friend_id = field[1]
                friend_first_name = field[3]
                friend_last_name = field[4]
                friend_alias = []
                if field[5]:
                    friend_alias = field[5]
        room_id = 'Autotest_group_id'+str(time.time()).split('.')[0]
        friend_member = member(container=Atom('chain'), phone_id=friend_id, names=friend_first_name,
                               surnames=friend_last_name, alias=friend_alias, status=Atom('member'))
        main_admin = member(container=Atom('chain'), phone_id=main_id, names=main_first_name, surnames=main_last_name,
                            alias=main_alias, status=Atom('admin'))
        room_data = []
        if group_avatar:
            avatar_module = Atom('Desc')
            avatar_id = 'Autotest_avatar' + str(time.time()).split('.')[0]
            mime = 'image'
            avatar_payload = "https://s3-us-west-2.amazonaws.com/nynja-defaults/Image_" \
                             "153310818583129_86FC1EF5-C297-4A1A-9FA1-A7D3C5E27E0E1533108186.jpg"
            parentid = []
            avatar_data = []
            room_data = [(avatar_module, avatar_id, mime, avatar_payload, parentid, avatar_data)]

        client.publish(topic="events/1//api/anon//", payload=bytearray(
            room(room_id=room_id,name=name,members=[bert.decode(friend_member)], admins=[bert.decode(main_admin)],
                 data=room_data, room_status=Atom('create'))), qos=2, retain=False)

    if data[0] == Atom('Room') and alias_check:
        log.info('Verify group created and alias exist')
        Verify.true((data[15][10][0][3] == user_id + b' created the group' and
                     ([field[0][11] for field in data if field and list == type(field) and int != type(field[0]) and
                       field[0][-1] == Atom("admin")][0] == main_first_name + main_last_name)),
                    "No message about creation")
        client.disconnect()

    elif data[0] == Atom('Room'):
        log.info("Verify group creation")
        Verify.true((data[15][10][0][3] == user_id + b' created the group' and
                     (data[8] != [] if avatar else True)), "No message about creation")
        client.disconnect()

    elif data == (Atom('io'), (Atom('error'), Atom('invalid_data')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise InvalidData("Invalid data response")

    elif data == (Atom('io'), (Atom('error'), Atom('permission_denied')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise PermissionDenied("No permission")

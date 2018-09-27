import bert
from erlastic import Atom
from models.roster_model import roster
from utils.convector import string_to_bytes
from utils.exception import InvalidData, PermissionDenied
from utils.logs import log
from utils.verify import Verify


def parser(client, payload, first_name=None, last_name=None, user_name=None, avatar=None):
    data = bert.decode(bytes(payload))

    if data[0] == Atom('Profile') and (data[-1]) == Atom('init'):
        roas = (bert.decode(bytes(payload))[3])
        userid = roas[0][1]
        if user_name:
            first_name = ''
            last_name = ''
            avatar = []
            status = Atom('nick')
        elif avatar:
            first_name = ''
            last_name = ''
            user_name = ''
            status = Atom('patch')
        else:
            avatar = []
            status = Atom('patch')
        client.publish(topic="events/1//api/anon//", payload=bytearray(
            roster(user_id=userid, first_name=first_name, last_name=last_name, my_username=user_name, avatar=avatar,
                   status=status)), qos=2, retain=False)

    if data[0] == Atom('Roster') and (data[-1]) == Atom('nick'):
        log.info("Verify roster/nick updated")
        Verify.true(data[5] == string_to_bytes(user_name), 'Username does not set')
        client.disconnect()

    elif data[0] == Atom('Roster') and (data[-1]) == Atom('patch') and avatar:
        log.info("Verify roster/avatar updated")
        Verify.true(data[11] == string_to_bytes(avatar), 'Username does not set')
        client.disconnect()

    elif data[0] == Atom('Roster') and (data[-1]) == Atom('patch'):
        log.info("Verify roster/name updated")
        Verify.true(data[2] == string_to_bytes(first_name), 'Username does not set')
        client.disconnect()

    elif data == (Atom('io'), (Atom('error'), Atom('invalid_data')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise InvalidData("Invalid data response")

    if data == (Atom('io'), (Atom('error'), Atom('permission_denied')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise PermissionDenied("No permission")

import bert
from erlastic import Atom
from models.update_name import update_name
from utils.logs import log


def parser(client, payload, first_name, last_name):
    data = bert.decode(bytes(payload))

    if data[0] == Atom('Profile') and (data[-1]) == Atom('init'):
        roas = (bert.decode(bytes(payload))[3])
        userid = roas[0][1]
        client.publish(topic="events/1//api/anon//", payload=bytearray(
            update_name(user_id=userid, first_name=first_name, last_name=last_name, status=Atom('patch'))), qos=2,
                       retain=False)

    elif data == (Atom('io'), (Atom('error'), Atom('invalid_data')), b''):
        log.error("Something going wrong")
        client.disconnect()

    if data == (Atom('io'), (Atom('error'), Atom('permission_denied')), b''):
        log.error("Something going wrong")
        client.disconnect()

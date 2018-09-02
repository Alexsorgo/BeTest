import bert
from erlastic import Atom
from requests import registration, sms


def parser(client, payload, my_number):
    firstname = 'first' + str(my_number)
    lastname = 'last' + str(my_number)
    data = bert.decode(bytes(payload))

    for node in data:
        if node == (Atom('ok'), Atom('sms_sent')):
            client.publish(topic="events/1//api/anon//", payload=bytearray(sms(my_number)), qos=2,
                           retain=False)

        if node == Atom('Profile') and (data[-1]) == Atom('init'):
            roas = (bert.decode(bytes(payload))[3])
            userid = roas[0][1]
            client.publish(topic="events/1//api/anon//", payload=bytearray(
                registration(userid, firstname, lastname)), qos=2, retain=False)

        if node == Atom('Roster') and (data[-1]) == Atom('patch'):
            assert data[2] == b'first'+bytes(str(my_number).encode('utf-8'))
            client.disconnect()

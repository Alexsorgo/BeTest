import bert
from erlastic import Atom
from requests import sms, search_by_phone


def parser(client, payload, threadNumber):
    data = bert.decode(bytes(payload))

    for node in data:
        if node == (Atom('ok'), Atom('sms_sent')):
            client.publish(topic="events/1//api/anon//", payload=bytearray(sms(threadNumber)), qos=2,
                           retain=False)

        if node == Atom('io') and data[1] == (Atom('ok'), b'phone'):
            if data[2][6]:
                print('Contact found')
                print(data[2][6])
                client.disconnect()
            if not data[2][6]:
                print('Contact not found')
                client.disconnect()

        if node == Atom('Profile') and data[8] == 'init':
            roas = (bert.decode(bytes(payload))[3])
            user_id = roas[0][1]
            search_phone = '38000000002'
            client.publish(topic="events/1//api/anon//", payload=bytearray(
                search_by_phone(user_id, search_phone)), qos=2, retain=False)

        if node == Atom('Roster'):
            print("Roaster Updated:" + str(threadNumber))
            client.disconnect()

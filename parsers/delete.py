import bert
from erlastic import Atom
from requests import sms, delete_user


def parser(client, payload, threadNumber):
    data = bert.decode(bytes(payload))

    for node in data:
        if node == (Atom('ok'), Atom('sms_sent')):
            client.publish(topic="events/1//api/anon//", payload=bytearray(sms(threadNumber)), qos=2,
                           retain=False)

        if node == Atom('Profile') and data[8] == 'remove':
            print('User {} deleted'.format(str(threadNumber)))
            client.disconnect()

        if node == Atom('Profile') and data[8] == 'init':
            client.publish(topic="events/1//api/anon//", payload=bytearray(
                delete_user(threadNumber)), qos=2, retain=False)

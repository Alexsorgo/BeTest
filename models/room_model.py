import bert
from erlastic import Atom
from utils.logs import log


def room(**data):
    module = Atom('Room')
    expected = ['room_id', 'name', 'links', 'description', 'settings', 'members', 'admins', 'data', 'room_type', 'tos',
                'tos_update', 'unread', 'mentions', 'readers', 'last_msg', 'update', 'created', 'room_status']
    actual = data
    my_dict = {}
    for i in expected:
        if i in actual.keys():
            my_dict.update({i: actual[i]})
        else:
            my_dict.update({i: []})

    request_f = (module, my_dict['room_id'], my_dict['name'], my_dict['links'], my_dict['description'],
                 my_dict['settings'], my_dict['members'], my_dict['admins'], my_dict['data'], my_dict['room_type'],
                 my_dict['tos'], my_dict['tos_update'], my_dict['unread'], my_dict['mentions'], my_dict['readers'],
                 my_dict['last_msg'], my_dict['update'], my_dict['created'], my_dict['room_status'])

    request = bert.encode(request_f)
    log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    return request

import bert
from erlastic import Atom
from utils.logs import log


def update_name(**data):
    module = Atom('Roster')
    expected = ['user_id', 'first_name', 'last_name', 'email', 'my_username', 'user_list', 'room_list', 'favorite',
                'tags', 'phone', 'avatar', 'update', 'status']
    actual = data
    my_dict = {}
    for i in expected:
        if i in actual.keys():
            my_dict.update({i: actual[i]})
        else:
            my_dict.update({i: []})

    request_f = (module, my_dict['user_id'], my_dict['first_name'], my_dict['last_name'], my_dict['email'],
                 my_dict['my_username'], my_dict['user_list'], my_dict['room_list'], my_dict['favorite'],
                 my_dict['tags'], my_dict['phone'], my_dict['avatar'], my_dict['update'], my_dict['status'])

    request = bert.encode(request_f)
    log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    log.debug("Updating First/Last names")
    return request

import bert
from erlastic import Atom
from utils.logs import log


def member(**data):
    module = Atom('Member')
    expected = ['member_id', 'container', 'feed_id', 'prev', 'next', 'feeds', 'phone_id', 'avatar', 'names', 'surnames',
                'alias', 'reader', 'update', 'settings', 'services', 'presence', 'status']
    actual = data
    my_dict = {}
    for i in expected:
        if i in actual.keys():
            my_dict.update({i: actual[i]})
        else:
            my_dict.update({i: []})

    request_f = (module, my_dict['member_id'], my_dict['container'], my_dict['feed_id'], my_dict['prev'],
                 my_dict['next'], my_dict['feeds'], my_dict['phone_id'], my_dict['avatar'], my_dict['names'],
                 my_dict['surnames'], my_dict['alias'], my_dict['reader'], my_dict['update'], my_dict['settings'],
                 my_dict['services'], my_dict['presence'], my_dict['status'])

    request = bert.encode(request_f)
    log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    log.debug("Send group creation request")
    return request


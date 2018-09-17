import bert
from erlastic import Atom
from utils.logs import log


def job(**data):
    module = Atom('Job')
    expected = ['id', 'container', 'feed_id', 'next', 'prev', 'context', 'proc', 'time', 'data', 'events', 'settings',
                'status']
    actual = data
    my_dict = {}
    for i in expected:
        if i in actual.keys():
            my_dict.update({i: actual[i]})
        else:
            my_dict.update({i: []})

    request_f = (module, my_dict['id'], my_dict['container'], my_dict['feed_id'], my_dict['next'], my_dict['prev'],
                 my_dict['context'], my_dict['proc'], my_dict['time'], my_dict['data'], my_dict['events'],
                 my_dict['settings'], my_dict['status'])

    by_phone = bert.encode(request_f)
    log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    return by_phone


def act(**kwargs):
    module = Atom('act')
    expected = ['name', 'data']
    actual = kwargs

    my_dict = {}
    for i in expected:
        if i in actual.keys():
            my_dict.update({i: actual[i]})
        else:
            my_dict.update({i: []})

    return module, my_dict['name'], my_dict['data']

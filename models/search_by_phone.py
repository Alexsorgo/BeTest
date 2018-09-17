import bert

from erlastic import Atom
from utils.logs import log


def search(**data):
    module = Atom('Search')
    expected = ['user_id', 'ref', 'field', 'type_r', 'value', 'status']
    actual = data
    my_dict = {}
    for i in expected:
        if i in actual.keys():
            my_dict.update({i: actual[i]})
        else:
            my_dict.update({i: []})

    request_f = (module, my_dict['user_id'], my_dict['ref'], my_dict['field'], my_dict['type_r'],
                 my_dict['value'], my_dict['status'])

    by_phone = bert.encode(request_f)
    # log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(by_phone_f)+'\r\n')
    log.debug("Search by number {}".format(str(my_dict['value'])))
    return by_phone

import bert

from erlastic import Atom
from utils.logs import log


def feature(**data):
    module = Atom('Feature')
    expected = ['id', 'key', 'value', 'group']
    actual = data
    my_dict = {}
    for i in expected:
        if i in actual.keys():
            my_dict.update({i: actual[i]})
        else:
            my_dict.update({i: []})

    request_f = (module, my_dict['id'], my_dict['key'], my_dict['value'], my_dict['group'])

    # request = bert.encode(request_f)
    # log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(by_phone_f)+'\r\n')
    return request_f

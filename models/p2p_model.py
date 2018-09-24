from erlastic import Atom


def p2p(**data):
    module = Atom('p2p')
    expected = ['from_user', 'to']
    actual = data
    my_dict = {}
    for i in expected:
        if i in actual.keys():
            my_dict.update({i: actual[i]})
        else:
            my_dict.update({i: []})

    request_f = (module, my_dict['from_user'], my_dict['to'])

    return request_f

import bert

from erlastic import Atom


def get_profile():
    module = Atom('Profile')
    phone_id = '817090909090'
    settings = []
    status = Atom('get')

    request_f = (module,phone_id,settings,settings,settings,settings,settings,settings,status)
    request = bert.encode(request_f)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    return request

""" {Profile,8613777322455,NIL,NIL,NIL,0,0,NIL,remove} """
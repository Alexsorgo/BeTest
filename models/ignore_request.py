import bert

from erlastic import Atom


def ignore_request():
    module = Atom('Friend')
    phone_id = '12566018988_727'            # phone_id  = [] :: [] | binary(),
    friend_id = '51997259024_549'                          # friend_id = [] :: [] | binary(),
    settings = []                           # settings  = [] :: list(#'Feature'{}),
    status = Atom('ignore')                 # status    = [] :: [] | ban | unban
                                            # | request | confirm | update
    request_f = (module,phone_id,friend_id,settings,status)
    request = bert.encode(request_f)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    return request

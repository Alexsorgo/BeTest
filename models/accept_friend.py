import bert

from erlastic import Atom


def accept_friend():
    module = Atom('Friend')
    phone_id = '51997259024_542'          # phone_id  = [] :: [] | binary(),
    friend_id = '12566018988_541'           # friend_id = [] :: [] | binary(),
    settings = []                           # settings  = [] :: list(#'Feature'{}),
    status = Atom('confirm')                # status    = [] :: [] | ban | unban
                                            # | request | confirm | update
    request_f = (module,phone_id,friend_id,settings,status)
    request = bert.encode(request_f)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    return request

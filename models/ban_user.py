import bert

from erlastic import Atom


def ban_user():
    module = Atom('Friend')
    phone_id = '8613151713157_881'            # phone_id  = [] :: [] | binary(),
    friend_id = '817090909090_841'                          # friend_id = [] :: [] | binary(),
    settings = []                           # settings  = [] :: list(#'Feature'{}),
    status = Atom('ban')                    # status    = [] :: [] | ban | unban
                                            # | request | confirm | update
    request_f = (module,phone_id,friend_id,settings,status)
    request = bert.encode(request_f)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    return request

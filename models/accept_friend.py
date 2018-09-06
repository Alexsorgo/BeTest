import bert

from erlastic import Atom
from utils.logs import log


def accept_friend(phone_id, friend_id):
    module = Atom('Friend')
    phone_id = phone_id                     # phone_id  = [] :: [] | binary(),
    friend_id = friend_id                   # friend_id = [] :: [] | binary(),
    settings = []                           # settings  = [] :: list(#'Feature'{}),
    status = Atom('confirm')                # status    = [] :: [] | ban | unban
                                            # | request | confirm | update
    request_f = (module,phone_id,friend_id,settings,status)
    request = bert.encode(request_f)
    # log.debug('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    log.debug("Accept friend request from {}".format(str(friend_id)))
    return request

import bert

from erlastic import Atom
from utils.logs import log


def invite_friend(main_id, friend_id):
    Friend = Atom('Friend')
    request = Atom('request')
    my_id = main_id
    friend_id = friend_id
    invite_f = (Friend,my_id,friend_id,[],request)
    by_phone = bert.encode(invite_f)
    # log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(invite_f)+'\r\n')
    log.debug("Send friend request to {}".format(str(friend_id)))
    return by_phone

import bert

from erlastic import Atom


def invite_friend():
    Friend = Atom('Friend')
    request = Atom('request')
    my_id = '380935940741_209'
    friend_id = '85269911852_42'
    invite_f = (Friend,my_id,friend_id,[],request)
    by_phone = bert.encode(invite_f)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(invite_f)+'\r\n')
    return by_phone

import bert

from erlastic import Atom


def search_by_username():
    module = Atom('Search')
    user_id = 123123                     # id     = [] :: [] | integer(),
    ref = 'username'                       # ref    = [] :: [] | binary(),
    field = 'nick'                     # field  = [] :: [] | binary(),
    type_r = Atom('==')                 # type   = [] :: [] | '==' | '!=' | 'like',
    value = ['UA']             # value  = [] :: [] | term(),
    status = Atom('contact')            # status = [] :: [] | profile | roster | contact | member | room
    by_phone_f = (module,user_id,ref,field,type_r,value,status)
    by_phone = bert.encode(by_phone_f)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(by_phone_f)+'\r\n')
    return by_phone

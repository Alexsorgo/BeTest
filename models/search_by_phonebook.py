import bert

from erlastic import Atom
from utils.logs import log


def search_by_phonebook(user_id, search_phone):
    module = Atom('Search')
    user_id = user_id                     # id     = [] :: [] | integer(),
    ref = 'phonebook'                       # ref    = [] :: [] | binary(),
    field = 'phone'                     # field  = [] :: [] | binary(),
    type_r = Atom('==')                 # type   = [] :: [] | '==' | '!=' | 'like',
    value = [search_phone]             # value  = [] :: [] | term(),
    status = Atom('contact')            # status = [] :: [] | profile | roster | contact | member | room
    by_phone_f = (module,user_id,ref,field,type_r,value,status)
    by_phone = bert.encode(by_phone_f)
    log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(by_phone_f)+'\r\n')
    return by_phone

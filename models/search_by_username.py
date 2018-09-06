import bert

from erlastic import Atom
from utils.logs import log


def search_by_username(user_id, search_username):
    module = Atom('Search')
    user_id = user_id                     # id     = [] :: [] | integer(),
    ref = 'username'                       # ref    = [] :: [] | binary(),
    field = 'nick'                     # field  = [] :: [] | binary(),
    type_r = Atom('==')                 # type   = [] :: [] | '==' | '!=' | 'like',
    value = [search_username]             # value  = [] :: [] | term(),
    status = Atom('contact')            # status = [] :: [] | profile | roster | contact | member | room
    by_phone_f = (module,user_id,ref,field,type_r,value,status)
    by_phone = bert.encode(by_phone_f)
    # log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(by_phone_f)+'\r\n')
    log.debug("Search by username {}".format(str(search_username)))
    return by_phone

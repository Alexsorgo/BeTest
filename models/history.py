import bert
from erlastic import Atom
from utils.logs import log


def history_schedule():
    model = Atom('History')
    user_id = '38000000001_13825'               # roster_id = [] :: [] | binary(),
    history_type = Atom('act')
    name = 'publish'                            # name = <<"publish">> :: [] | binary(),
    dt = '38000000001_13825'                    # data = []:: binary() | integer() | list(term())})
    action = Atom('get')
    size = []                                   # size      = 0 :: [] | integer(),
    entity_id = []                              # entity_id = 0 :: [] | integer(),
    data = []                                   # data      = [] :: list(#'Message'{}) | list(#'Job'{}),
    request_f = (model,user_id,(history_type,name,dt),size,entity_id,data,action)
    request = bert.encode(request_f)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    return request


def history_p2p():
    model = Atom('History')
    user_id = '8613777322455_544'               # roster_id = [] :: [] | binary(),
    history_type = Atom('p2p')
    from_r = '12566018988_541'                # from = [] :: [] | binary(),
    to_r = '51997259024_542'                    # to   = [] :: [] | binary()
    action = Atom('get')
    size = -15                                  # size      = 0 :: [] | integer(),
    entity_id = 20483                           # entity_id = 0 :: [] | integer(),
    data = []                                   # data      = [] :: list(#'Message'{}) | list(#'Job'{}),
    request_f = (model,user_id,(history_type,from_r,to_r),size,entity_id,data,action)
    request = bert.encode(request_f)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    return request


def history_group(user_id, group_id):
    model = Atom('History')
    user_id = user_id               # roster_id = [] :: [] | binary(),
    history_type = Atom('muc')
    group_id = group_id                # group_id = [] :: [] | binary(),
    size = []                                  # size      = 0 :: [] | integer(),
    entity_id = []                           # entity_id = 0 :: [] | integer(),
    data = []                                   # data      = [] :: list(#'Message'{}) | list(#'Job'{}),
    action = Atom('delete')
    request_f = (model,user_id,(history_type,group_id),size,entity_id,data,action)
    request = bert.encode(request_f)
    # log.debug('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    log.debug('Clear group chat history request')
    return request

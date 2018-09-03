import bert
import time

from erlastic import Atom


def send_message():
    module = Atom('Message')
    id_r = []                                                               # id        = [] :: [] | integer(),
    container = Atom('chain')                                               # container = chain :: atom() | chain | cur,
    p2p_from = '380998681837_437'
    p2p_to = '8613777322455_544'
    feed_id = (Atom('p2p'),p2p_from,p2p_to)                                 # feed_id   = [] :: #muc{} | #p2p{},
    prev = []                                                               # prev      = [] :: [] | integer(),
    next_r = []                                                             # next      = [] :: [] | integer(),
    msg_id = 'Autotest_security'+str(time.time()).split('.')[0]        # msg_id    = [] :: [] | binary(),
    from_r2 = '380998681837_437'                                           # from      = [] :: [] | binary(),
    to_r2 = '8613777322455_544'                                               # to        = [] :: [] | binary(),
    created = int(str(time.time()).split('.')[0])                          # created   = [] :: [] | integer() | binary
    '''=======DESC MODEL======='''
    desc_module = Atom('Desc')
    desc_id = 'Autotest_security'+str(time.time()).split('.')[0]       # id       = [] :: [] | binary(),
    desc_mime = 'text'                                                      # mime     = <<"text">> :: binary(),
    desc_payload = 'Hello'                                                 # payload  = [] :: [] | binary(),
    parentid = []                                                           # parentid = [] :: [] | binary(),
    data = []                                                               # data     = [] :: list(#'Feature'{})
    '''===========END=========='''
    files = (desc_module,desc_id,desc_mime,desc_payload,parentid,data)      # files     = [] :: [] | list(#'Desc'{}),
    type_m = []                                                             # type      = [] :: [] | [atom() | sys | reply | forward | sched | read | edited],
    link = []                                                               # link      = [] :: [] | integer(),
    seenby = []                                                             # seenby    = [] :: [] |  list(binary() | integer()),
    repliedby = []                                                          # repliedby = [] :: [] | list(integer()),
    mentioned = []                                                          # mentioned = [] :: [] | list(integer()),
    status = []                                                             # status    = [] :: [] | delete | clear | update | edit
    request_f = (module,id_r,container,feed_id,prev,next_r,msg_id,from_r2,to_r2,created,[files],
                 type_m,link,seenby,repliedby,mentioned,status)
    request = bert.encode(request_f)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    asd = []
    for i in request:
        asd.append(i)
    print(asd)
    return request

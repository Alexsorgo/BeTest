import bert
import time

from erlastic import Atom


def send_message():
    module = Atom('Message')
    id_r = []                                                               # id        = [] :: [] | integer(),
    container = Atom('chain')                                               # container = chain :: atom() | chain | cur,
    p2p_from = '817090909090_841'
    p2p_to = '8613151713157_896'
    feed_id = (Atom('p2p'),p2p_from,p2p_to)                                 # feed_id   = [] :: #muc{} | #p2p{},
    prev = []                                                               # prev      = [] :: [] | integer(),
    next_r = []                                                             # next      = [] :: [] | integer(),
    msg_id = 'Autotest_message_id_'+str(time.time()).split('.')[0]        # msg_id    = [] :: [] | binary(),
    from_r2 = '8613151713157_896'                                           # from      = [] :: [] | binary(),
    to_r2 = '817090909090_841'                                               # to        = [] :: [] | binary(),
    created = int(str(time.time()).split('.')[0])                          # created   = [] :: [] | integer() | binary
    '''=======DESC MODEL======='''
    desc_module = Atom('Desc')
    desc_id = 'Autotest_desc_id_'+str(time.time()).split('.')[0]       # id       = [] :: [] | binary(),
    desc_mime = 'text'                                                      # mime     = <<"text">> :: binary(),
    desc_payload = 'вафли'                                                 # payload  = [] :: [] | binary(),
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

    r = (Atom('Message'), [], Atom('chain'), (Atom('p2p'), b'817090909090_168', b'8613151713157_167'), [], [], 'Autotest_security1536582453', b'817090909090_168', b'8613151713157_167', [], [(Atom('Desc'), 'Autotest_security1536582453', 'thumb', 'https://s3-us-west-2.amazonaws.com/nynja-defaults/thumb_153657407372743_9B03C956-E679-4541-BE9A-86A710290131.jpg', [], [(Atom('Feature'), '2EC12976-9521-48E7-9898-D1CE304CD34F_8613777322455_655_size_31E96AB9-A4DB-4538-B93B-3987C24D3FC5_153657407840657', 'SIZE', '64575', 'FILE_DATA'), (Atom('Feature'), '2EC12976-9521-48E7-9898-D1CE304CD34F_8613777322455_655_filename_D185367A-5103-404F-B51A-7C89F99C738B_153657407840569', 'FILENAME', 'thumb_153657407372743_9B03C956-E679-4541-BE9A-86A710290131.jpg', 'FILE_DATA'), (Atom('Feature'), '2EC12976-9521-48E7-9898-D1CE304CD34F_8613777322455_655_resolution_1074DE19-A186-4D7D-8719-BC439C15D4AC_153657407374066', 'RESOLUTION', '256:171', 'FILE_DATA')])], [], [], [], [], [], [])
    request = bert.encode(r)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(r)+'\r\n')
    # asd = []
    # for i in request:
    #     asd.append(i)
    # print(asd)
    return request

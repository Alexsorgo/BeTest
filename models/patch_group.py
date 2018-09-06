import bert

from erlastic import Atom
from utils.logs import log


def patch_group(room_id, room_name):
    module = Atom('Room')
    room_id = room_id                                               # id          = [] :: [] | binary(),
    name = room_name                                                # name        = [] :: [] | binary(),
    links = []
    description = []                                                # description = [] :: [] | binary(),
    settings = []                                                   # settings    = [] :: list(),
    members = []                                                    # members     = [] :: list(#'Member'{}),
    admins = []                                                     # admins      = [] :: list(#'Member'{}),
    data = []                                                       # data        = [] :: [] | list(#'Desc'{}),
    room_type = []                                                  # type        = [] :: [] | atom() | group | channel,
    tos = []                                                        # tos         = [] :: [] | binary(),
    tos_update = []                                                 # tos_update  = 0  :: [] | integer(),
    unread = []                                                     # unread      = 0  :: [] | integer(),
    mentions = []                                                   # mentions    = [] :: [] | list(integer()),
    readers = []                                                    # readers     = [] :: list(integer()),
    last_msg = []                                                   # last_msg    = [] :: [] | #'Message'{},
    update = []                                                     # update      = 0  :: [] | integer(),
    created = []                                                    # created     = 0  :: [] | integer(),
    room_status = Atom('patch')                                    #  status      = [] :: [] | create | leave| add | remove | patch | get | delete | last_msg}).

    request_f = (module,room_id,name,links,description,settings,members,admins,data,room_type,
                 tos,tos_update,unread,mentions,readers,last_msg,update,created,room_status)

    request = bert.encode(request_f)
    # log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    log.debug("Send group creation request")
    return request

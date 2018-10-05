import bert
import time

from erlastic import Atom
from models.member import member
from utils.data_generation import magic
from utils.logs import log


def create_group(main_id, main_firstname, main_lastname, main_alias, friend_id,
                 friend_firstname, friend_lastname, friend_alias, group_avatar):
    module = Atom('Room')
    room_id = 'Autotest_group_id'+str(time.time()).split('.')[0]        # id          = [] :: [] | binary(),
    name = magic.get_word                                            # name        = [] :: [] | binary(),
    links = []
    description = []                                                    # description = [] :: [] | binary(),
    settings = []                                                       # settings    = [] :: list(),

    friend_member = member(container=Atom('chain'), phone_id=friend_id, names=friend_firstname, surnames=friend_lastname,
                           alias=friend_alias, status=Atom('member'))
    main_admin = member(container=Atom('chain'), phone_id=main_id, names=main_firstname, surnames=main_lastname,
                        alias=main_alias, status=Atom('admin'))

    members = [bert.decode(friend_member)]                          # members     = [] :: list(#'Member'{}),
    admins = [bert.decode(main_admin)]                              # admins      = [] :: list(#'Member'{}),
    data = []                                                       # data        = [] :: [] | list(#'Desc'{}),
    room_type = Atom('group')                                       # type        = [] :: [] | atom() | group | channel,
    tos = []                                                        # tos         = [] :: [] | binary(),
    tos_update = []                                                 # tos_update  = 0  :: [] | integer(),
    unread = []                                                     # unread      = 0  :: [] | integer(),
    mentions = []                                                   # mentions    = [] :: [] | list(integer()),
    readers = []                                                    # readers     = [] :: list(integer()),
    last_msg = []                                                   # last_msg    = [] :: [] | #'Message'{},
    update = []                                                     # update      = 0  :: [] | integer(),
    created = []                                                    # created     = 0  :: [] | integer(),
    room_status = Atom('create')                                    # status      = [] :: [] | create | leave| add | remove | patch | get | delete | last_msg}).
    if group_avatar:
        avatar_module = Atom('Desc')
        avatar_id = 'Autotest_avatar'+str(time.time()).split('.')[0]
        mime = 'image'
        avatar_payload = "https://s3-us-west-2.amazonaws.com/nynja-defaults/Image_" \
                         "153310818583129_86FC1EF5-C297-4A1A-9FA1-A7D3C5E27E0E1533108186.jpg"
        parentid = []
        avatar_data = []
        data = [(avatar_module,avatar_id,mime,avatar_payload,parentid,avatar_data)]

    request_f = (module,room_id,name,links,description,settings,members,admins,data,room_type,
                 tos,tos_update,unread,mentions,readers,last_msg,update,created,room_status)

    request = bert.encode(request_f)
    log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    log.debug("Send group creation request")
    log.debug(request_f)
    return request

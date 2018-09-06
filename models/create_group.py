import bert
import time

from configs import config
from erlastic import Atom
from utils.data_generation import magic
from utils.logs import log


def create_group(main_id, main_firstname, main_lastname, main_alias, friend_id,
                 friend_firstname, friend_lastname, friend_alias, group_avatar):
    module = Atom('Room')
    room_id = 'Autotest_security'+str(time.time()).split('.')[0]        # id          = [] :: [] | binary(),
    name = magic.get_word                                            # name        = [] :: [] | binary(),
    links = []
    description = []                                                    # description = [] :: [] | binary(),
    settings = []                                                       # settings    = [] :: list(),
    '''======== MEMBER MODEL ======='''
    member_module = Atom('Member')
    member_id = []
    container = Atom('chain')
    feed_id = []
    prev = []
    member_next = []
    feeds = []
    phone_id_1 = main_id
    phone_id_2 = friend_id
    avatar = []
    names_1 = main_firstname
    surnames_1 = main_lastname
    alias_1 = main_alias
    names_2 = friend_firstname
    surnames_2 = friend_lastname
    alias_2 = friend_alias
    reader = []
    update = []
    member_settings = []
    member_services = []
    presence = []
    member_status_1 = Atom('member')
    member_status_2 = Atom('member')
    member_status_3 = Atom('admin')
    '''============ END ============'''
    member1 = (member_module,member_id,container,feed_id,prev,member_next,feeds,phone_id_1,avatar,
               names_1,surnames_1,alias_1,reader,update,member_settings,member_services,presence,member_status_1)
    member2 = (member_module,member_id,container,feed_id,prev,member_next,feeds,phone_id_2,avatar,
               names_2,surnames_2,alias_2,reader,update,member_settings,member_services,presence,member_status_2)
    member3 = (member_module, member_id, container, feed_id, prev, member_next, feeds, phone_id_1, avatar,
               names_1, surnames_1, alias_1, reader, update, member_settings, member_services, presence,
               member_status_3)
    members = [member2]                                    # members     = [] :: list(#'Member'{}),
    admins = [member3]                                              # admins      = [] :: list(#'Member'{}),
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
    room_status = Atom('create')                                    #  status      = [] :: [] | create | leave| add | remove | patch | get | delete | last_msg}).
    if group_avatar:
        avatar_module = Atom('Desc')
        avatar_id = 'Autotest_avatar'+str(time.time()).split('.')[0]
        mime = 'image'
        # avatar_payload = "https://s3-us-west-2.amazonaws.com/nynja-defaults/Image_153310818583129_86FC1EF5-C297-4A1A-9FA1-A7D3C5E27E0E1533108186.jpg"
        avatar_payload = "https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-682370.jpg"
        parentid = []
        avatar_data = []
        data = [(avatar_module,avatar_id,mime,avatar_payload,parentid,avatar_data)]

    request_f = (module,room_id,name,links,description,settings,members,admins,data,room_type,
                 tos,tos_update,unread,mentions,readers,last_msg,update,created,room_status)

    request = bert.encode(request_f)
    # log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    log.debug("Send group creation request")
    return request

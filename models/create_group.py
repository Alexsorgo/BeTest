import bert
import time

from erlastic import Atom


def create_group(main_id, main_firstname, main_lastname, main_alias, friend_id,
                 friend_firstname, friend_lastname, friend_alias):
    module = Atom('Room')
    room_id = 'Autotest_security'+str(time.time()).split('.')[0]  # id          = [] :: [] | binary(),
    name = 'Test group'                                                 # name        = [] :: [] | binary(),
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

    request_f = (module,room_id,name,links,description,settings,members,admins,data,room_type,
                 tos,tos_update,unread,mentions,readers,last_msg,update,created,room_status)

    request = bert.encode(request_f)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    return request

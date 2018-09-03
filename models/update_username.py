import bert
from erlastic import Atom


def update_username():
    model = Atom('Roster')
    user_id = 544                           # id       = [] :: [] | integer(),
    first_name = []                         # names    = [] :: [] | binary(),
    last_name = []                          # surnames = [] :: [] | binary(),
    email = []                              # email    = [] :: [] | binary(),
    my_username = 'Вафли'                  # nick     = [] :: [] | binary(),
    user_list = []                          # userlist = [] :: list(#'Contact'{}),
    room_list = []                          # roomlist = [] :: list(#'Room'{}),
    favorite = []                           # favorite = [] :: list(#'ExtendedStar'{}),
    tags = []                               # tags     = [] :: list(#'Tag'{}),
    phone = []                              # phone    = [] :: [] | binary(),
    avatar = []                             # avatar   = [] :: [] | binary(),
    update = []                             # update   = 0  :: [] | integer(),
    status = Atom('nick')                   # status   = [] :: [] | get | create | del | remove | nick | add | update
                                                               #  | list | patch | last_msg
    request_f = (model,user_id,first_name,last_name,email,my_username,user_list,room_list,favorite,
                 tags,phone,avatar,update,status)
    request = bert.encode(request_f)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    return request
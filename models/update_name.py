import bert
from erlastic import Atom


def update_name():

    user_name = []
    model = Atom('Roster')
    user_id = 168                           # id       = [] :: [] | integer(),
    first_name = 'Sergey'                    # names    = [] :: [] | binary(),
    last_name = []                      # surnames = [] :: [] | binary(),
    email = []                             # email    = [] :: [] | binary(),
    my_username = []                        # nick     = [] :: [] | binary(),
    user_list = []                          # userlist = [] :: list(#'Contact'{}),
    room_list = []                          # roomlist = [] :: list(#'Room'{}),
    favorite = []                           # favorite = [] :: list(#'ExtendedStar'{}),
    tags = []                               # tags     = [] :: list(#'Tag'{}),
    phone = '380935940741'                              # phone    = [] :: [] | binary(),
    avatar = []                             # avatar   = [] :: [] | binary(),
    update = []                             # update   = 0  :: [] | integer(),
    status = Atom('create')                  # status   = [] :: [] | get | create | del | remove | nick | add | update
                                                               #  | list | patch | last_msg
    request_f = (model, user_id, first_name, last_name, email, my_username, user_list, room_list, favorite,
                 tags, phone, avatar, update, status)
    # request_f = (Atom('Roster'), 72, b'new', b'some', [], [],
    #              [(Atom('Contact'), b'380977917979_71', [], b'Sergey', [], [], [2675, 2675], 0,
    #                (Atom('Message'), 2675, Atom('chain'), (Atom('p2p'), b'380935940741_72', b'380977917979_71'), [], [],
    #                 [], b'380935940741_72', b'380977917979_71', 1538400148192,
    #                 [(Atom('Desc'), b'srv_2675', b'text', b'', [], [])], [Atom('sys')], [], [], [], [], []),
    #                1538400155875, 1538400148193, [(Atom('Feature'), b'0C48BC01-B7C9-4B41-BEC7-53655D8E1C0C_380935940741'
    #                                                                 b'_72_CHAT_LANGUAGE_BA8BE284-8413-4D9D-A4D3-B54B8EF'
    #                                                                 b'DD74F_153840014989235', b'CHAT_LANGUAGE',
    #                                                b'English:en', b'LANGUAGE_SETTING')], [], Atom('online'),
    #                Atom('friend')), (Atom('Contact'), b'380935940741_72', [], b'new', b'some', [], b'\x00\x00', 0, b'',
    #                                  1538400100090, 0, [], [], Atom('online'), Atom('friend'))], [], [], [],
    #              b'380977917979', [], [], status)

    request = bert.encode(request_f)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    return request

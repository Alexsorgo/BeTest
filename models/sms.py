import bert

from erlastic import Atom
from utils.logs import log


def sms(main_number):
    phone_num = main_number
    module = Atom('Auth')
    client_id = []                                  # client_id   = [] :: [] | binary(),
    dev_key = phone_num                             # dev_key     = [] :: [] | binary(),
    user_id = []                                    # user_id     = [] :: [] | binary(),
    phone = phone_num                               # phone       = [] :: [] | binary(),
    token = []                                      # token       = [] :: [] | binary(),
    sms_code = '903182'                             # type        = [] :: [] | atom(),
    type_r = Atom('verify')                         # sms_code    = [] :: [] | binary(),
    attempts = []                                   # attempts    = [] :: [] | integer(),
    services = []                                   # services    = [] :: list(atom()),
    settings = [('Feature', "id_DEFAULT_LANGUAGE", "DEFAULT_LANGUAGE", "English:en", "LANGUAGE_SETTING")]
    push = []                                       # push        = [] :: [] | binary(),
    os = []                                         # os          = [] :: [] | atom() | ios | android | web,
    created = []                                    # created     = [] :: [] | integer() | binary(),
    last_online = []                                # last_online = [] :: [] | integer()})
    request_f = (module, client_id, dev_key, user_id, phone, token, type_r, sms_code, attempts, services,
                 settings, push, os, created, last_online)
    request = bert.encode(request_f)
    # log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    log.debug("Send sms verify")
    return request

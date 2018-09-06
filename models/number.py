import bert

from erlastic import Atom
from utils.logs import log


def login(main_number):
    phone_num = main_number
    feature = Atom('Feature')
    module = Atom('Auth')
    client_id = "reg_"+phone_num                    # client_id   = [] :: [] | binary(),
    dev_key = phone_num                             # dev_key     = [] :: [] | binary(),
    user_id = []                                    # user_id     = [] :: [] | binary(),
    phone = phone_num                               # phone       = [] :: [] | binary(),
    token = []                                      # token       = [] :: [] | binary(),
    sms_code = []                                   # type        = [] :: [] | atom(),
    type_r = Atom('reg')                            # sms_code    = [] :: [] | binary(),
    attempts = []                                   # attempts    = [] :: [] | integer(),
    services = []                                   # services    = [] :: list(atom()),
                                                    # settings    = [] :: [] | list(#'Feature'{}),
    settings = [(feature, phone_num+"__152775413346297", "AppVersion", "0.2.95", "AUTH_DATA"),
                (feature, phone_num+"__152775413346297", "OS", "iOS 11.3", "AUTH_DATA"),
                (feature, phone_num+"__152775413346297", "DeviceModel", "simulator/sandbox", "AUTH_DATA")]
    push = []                                       # push        = [] :: [] | binary(),
    os = []                                         # os          = [] :: [] | atom() | ios | android | web,
    created = []                                    # created     = [] :: [] | integer() | binary(),
    last_online = []                                # last_online = [] :: [] | integer()})
    request_f = (module,client_id,dev_key,user_id,phone,token,type_r,sms_code,attempts,services,
                 settings,push,os,created,last_online)
    request = bert.encode(request_f)
    # log.info('='*5 + 'REQUEST' + '='*5 + '\r\n' + str(request_f)+'\r\n')
    log.debug("Send Auth/check")
    return request

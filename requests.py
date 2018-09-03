import bert
from erlastic import Atom
from utils.logs import log


def login(phone_num):
    Auth = Atom('Auth')
    Feature = Atom('Feature')
    reg = Atom('reg')
    stri = (Auth, "reg_"+phone_num, phone_num, [], phone_num, [], reg, [], [], [], [(Feature, phone_num+"__152775413346297", "AppVersion", "0.2.95", "AUTH_DATA"), (Feature, phone_num+"__152775413346297", "OS", "iOS 11.3", "AUTH_DATA"), (Feature, phone_num+"__152775413346297", "DeviceModel", "simulator/sandbox", "AUTH_DATA")], [], [], [], [])
    login = bert.encode(stri)
    log.info('=' * 5 + 'REQUEST' + '=' * 5 + '\r\n' + str(stri) + '\r\n')
    return login


def sms(phone_num):
    Auth = Atom('Auth')
    verify = Atom('verify')
    sms_f = (Auth,[],phone_num,[],phone_num,[],verify,"903182",[],[],[],[],[],[],[])
    sms = bert.encode(sms_f)
    log.info('=' * 5 + 'REQUEST' + '=' * 5 + '\r\n' + str(sms_f) + '\r\n')
    return sms


def registration(userid, firstname, lastname):
    Roster = Atom('Roster')
    patch = Atom('patch')
    username_f = (Roster,int(userid),firstname,lastname,[],[],[],[],[],[],[],[],[],patch)
    username = bert.encode(username_f)
    log.info('=' * 5 + 'REQUEST' + '=' * 5 + '\r\n' + str(username_f) + '\r\n')
    return username


def delete_user(phone_number):
    Profile = Atom('Profile')
    remove = Atom('remove')
    user_delete_f = (Profile, phone_number,[],[],[],[],[],[],remove)
    log.info('=' * 5 + 'REQUEST' + '=' * 5 + '\r\n' + str(user_delete_f) +'\r\n')
    user_delete = bert.encode(user_delete_f)
    return user_delete


def search_by_phone(user_id, search_ph):
    Search = Atom('Search')
    contact = Atom('contact')
    equl = Atom('==')
    by_phone_f = (Search,user_id,'phone','phone',equl,[search_ph],contact)
    by_phone = bert.encode(by_phone_f)
    log.info('=' * 5 + 'REQUEST' + '=' * 5 + '\r\n' + str(by_phone_f) +'\r\n')
    return by_phone


def invite_friend(my_id, friend_id):
    Friend = Atom('Friend')
    request = Atom('request')
    invite_f = (Friend,my_id,friend_id,[],request)
    by_phone = bert.encode(invite_f)
    log.info('=' * 5 + 'REQUEST' + '=' * 5 + '\r\n' + str(invite_f) +'\r\n')
    return by_phone

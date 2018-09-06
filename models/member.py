import bert
from erlastic import Atom
from utils.logs import log


def member(new_alias):
    module = Atom('Member')
    id = []
    container = Atom('chain')
    feed_id = []
    prev = []
    next = []
    feeds = []
    phone_id = []
    avatar = []
    names = []
    surnames = []
    alias = new_alias
    reader = []
    update = []
    settings = []
    services = []
    presence = []
    status = Atom('patch')
    request_f = (module, id, container, feed_id, prev, settings, next, feeds, phone_id, avatar,
                 names, surnames, alias, reader, update, settings, services, presence, status)

    request = bert.encode(request_f)
    # log.info('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    log.debug("Send group creation request")
    return request

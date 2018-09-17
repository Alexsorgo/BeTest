from erlastic import Atom
import time


def desc_model(mime, payload, data):
    desc_module = Atom('Desc')
    desc_id = 'Autotest_desc_id' + str(time.time()).split('.')[0]
    desc_mime = mime
    desc_payload = payload
    parentid = []
    data = data
    return desc_module, desc_id, desc_mime, desc_payload, parentid, data
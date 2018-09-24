import bert
import time

from enums import enums
from erlastic import Atom
from models.desc import desc_model
from utils.data_generation import magic
from utils.logs import log

timestamp_time = str(time.time()).split('.')[0]


def message_model(mime, message_text=None, **kwargs):
    module = Atom('Message')
    msg_id = 'Autotest_message_id_' + timestamp_time
    if mime in enums.mime:
        if mime == 'audio':
            payload = "https://s3-us-west-2.amazonaws.com/nynja-defaults/A8CE6719-EB5E-4D8D-BF3E-5B5377463A73_" \
                      "380977917979_240_380667578356_623_153302368105645_361B7E18-302C-469D-BC86-9EF954E28179.mp3"
            features = [(Atom('Feature'), 'Feature_DURATION_'+timestamp_time, 'DURATION',
                         '50000', 'FILE_DATA'), (Atom('Feature'), 'Feature_INFO_'+timestamp_time, 'INFO',
                                                 '[0.00694619, 0.00598051, 0.00640373, 0.00411694, 0.00376302, '
                                                 '0.00385633, 0.00388491, 0.00562793, 0.00556369, 0.00590717, '
                                                 '0.00427526, 0.00305555, 0.00245941, 0.00367912, 0.0020681, '
                                                 '0.00200623, 0.00172327, 0.00153149, 0.00197051, 0.00254462, '
                                                 '0.00124885, 0.0190442, 0.0110677, 0.00437577, 0.0332922, 0.0111691,'
                                                 ' 0.00486005, 0.00158101, 0.0013417, 0.00131789, 0.00140617,'
                                                 ' 0.00129963, 0.00131394, 0.00181012, 0.0018368, 0.00159087, '
                                                 '0.00116367, 0.00132543, 0.00125508, 0.00166154, 0.00189293, '
                                                 '0.00109495, 0.00113848, 0.00128676, 0.00201494, 0.00321521, '
                                                 '0.00129334, 0.00115214, 0.00152102, 0.00297446, 0.00526876, '
                                                 '0.00282387, 0.00194889, 0.0026418, 0.00224314, 0.00122276, '
                                                 '0.00119336, 0.000969137, 0.000954979, 0.0010043, 0.00112306, '
                                                 '0.00074907, 0.00112774, 0.00106222, 0.00108591, 0.00102118, '
                                                 '0.00108384, 0.00132377, 0.00195076, 0.00223557, 0.00235106, '
                                                 '0.00229124, 0.0017405, 0.00125239, 0.000841596, 0.000576772, '
                                                 '.000592627, 0.000601461, 0.000991837, 0.00103431, 0.00111168, '
                                                 '0.000606259, 0.000560362, 0.000567207, 0.000628491, 0.000589819, '
                                                 '0.000622787, 0.000529032, 0.000557232, 0.000599589, 0.000763404, '
                                                 '0.000702032, 0.000524995, 0.000689804, 0.00060228, 0.000614362, '
                                                 '0.0021555, 1.0, 0.462762, 0.18173]', 'FILE_DATA'),
                        (Atom('Feature'), 'Feature_LANGUAGE_'+timestamp_time, 'LANGUAGE', 'en', 'FILE_DATA')]
            files = desc_model(mime, payload, features)

        if mime == 'text':
            if message_text:
                payload = message_text
            else:
                payload = magic.get_word
            features = []
            files = desc_model(mime, payload, features)

        if mime == 'image':
            payload = "https://s3-us-west-2.amazonaws.com/nynja-defaults/thumb" \
                      "_153657407372743_9B03C956-E679-4541-BE9A-86A710290131.jpg"
            features = [(Atom('Feature'), 'Feature_SIZE_'+timestamp_time, 'SIZE', '64575', 'FILE_DATA'),
                        (Atom('Feature'), 'Feature_FILENAME_'+timestamp_time, 'FILENAME',
                         'thumb_153657407372743_9B03C956-E679-4541-BE9A-86A710290131.jpg', 'FILE_DATA'),
                        (Atom('Feature'), 'Feature_RESOLUTION_'+timestamp_time, 'RESOLUTION', '256:171',
                         'FILE_DATA')]
            files = desc_model(mime, payload, features)

        if mime == 'video':
            payload = "https://s3-us-west-2.amazonaws.com/nynja-defaults/" \
                      "tmp_1536658896_B3C85DE6-D7BE-4870-BD03-BDC69FDFE0EF.mp4"
            features = [
                (Atom('Feature'), 'Feature_SIZE_'+timestamp_time, 'SIZE', '22935809', 'FILE_DATA'),
                (Atom('Feature'), 'Feature_DURATION_'+timestamp_time, 'DURATION', '58000', 'FILE_DATA'),
                (Atom('Feature'), 'Feature_FILENAME_'+timestamp_time, 'FILENAME', 'tmp_1536658896_B3C85DE6-D7BE-4870-'
                                                                                 'BD03-BDC69FDFE0EF.mp4', 'FILE_DATA')]
            files = desc_model(mime, payload, features)

        if mime == 'location':
            payload = "37.785834,-122.406417"
            features = []
            files = desc_model(mime, payload, features)

        if mime == 'sticker':
            payload = "https://s3.eu-central-1.amazonaws.com/sticker-packs/defaults/ny1.png"
            features = []
            files = desc_model(mime, payload, features)

    expected = ['id', 'container', 'feed_id', 'prev', 'next', 'from_user', 'to', 'created','type', 'link', 'seenby',
                'repliedby', 'mentioned', 'status']
    actual = kwargs
    my_dict = {}
    for i in expected:
        if i in actual.keys():
            my_dict.update({i: actual[i]})
        else:
            my_dict.update({i: []})

    request_f = (module, my_dict['id'], my_dict['container'], my_dict['feed_id'], my_dict['prev'], my_dict['next'],
                 msg_id, my_dict['from_user'], my_dict['to'], my_dict['created'], [files],
                 my_dict['type'], my_dict['link'], my_dict['seenby'], my_dict['repliedby'], my_dict['mentioned'],
                 my_dict['status'])
    request = bert.encode(request_f)
    log.debug('=' * 5 + 'REQUEST' + '=' * 5 + '\r\n' + str(request_f) + '\r\n')
    return request

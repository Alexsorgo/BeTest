import bert

from erlastic import Atom


def delete_user(phone_number):
    Profile = Atom('Profile')
    remove = Atom('remove')
    user_delete_f = (Profile, phone_number,[],[],[],[],[],[],remove)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(user_delete_f)+'\r\n'
          )
    user_delete = bert.encode(user_delete_f)
    return user_delete
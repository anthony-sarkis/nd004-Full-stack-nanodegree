import random
import string


def secure():
    salt = 'apple2'
    secure = ''.join(random.choice(string.ascii_uppercase + string.digits
                                   + salt) for x in xrange(32))
    return secure

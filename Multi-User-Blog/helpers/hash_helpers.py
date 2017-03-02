import string
import hashlib
import hmac
import random

# Hashing and password functions
# normally would not store in this file
SECRET = 'applesauce'


# call hmac passing secret phrase and phrase variable
def hash_str(s):
    x = hmac.new(SECRET, s).hexdigest()
    return x


# Return string with hash and value
def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))


# Check if cookie hash value equals real hash
def check_secure_val(h):
    x = h.split('|')[0]
    if make_secure_val(x) == h:
        return x


# Salt for password hash
def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))


# Make password hash
def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    # Create the sha256 hash using combo of name, password, and salt
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)


# Verify password by matching
def valid_pw(name, pw, h):
    # Split apart the salt from the hash
    salt = h.split(',')[1]
    # Determine if password is valid by comparing new hash to old hash
    return make_pw_hash(name, pw, salt) == h
    # return true
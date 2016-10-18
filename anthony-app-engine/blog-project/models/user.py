from google.appengine.ext import db
from helpers import hash_helpers

def users_key(group='default'):
    return db.Key.from_path('users', group)

class User(db.Model):
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    email = db.StringProperty()

    # functions
    @classmethod
    def by_id(cls, uid):
        # get by id is built in
        return User.get_by_id(uid, parent=users_key())

    @classmethod
    def by_name(cls, name):
        # return by name, basically select all by name where user =
        u = User.all().filter('name =', name).get()
        return u

    @classmethod
    def register(cls, name, pw, email=None):
        # Make password hash
        pw_hash = hash_helpers.make_pw_hash(name, pw)
        # Return user, with pw_hash instead of pw
        return User(parent=users_key(),
                    name=name,
                    pw_hash=pw_hash,
                    email=email)

    @classmethod
    def login(cls, name, pw):
        # Calls class method by name pass name
        u = cls.by_name(name)
        # check if user has valid password
        if u and hash_helpers.valid_pw(name, pw, u.pw_hash):
            return u


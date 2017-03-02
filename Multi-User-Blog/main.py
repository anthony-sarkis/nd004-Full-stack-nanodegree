#!/usr/bin/env python
import os
import webapp2
import jinja2
import re
import string
from helpers import hash_helpers
from google.appengine.ext import db

from models import user, post, comment
from helpers import hash_helpers
from handlers import handler, blogfront, deletecomment, deletepost, editcomment, editpost 
from handlers import likepost, login, logout, newcomment, newpost, postpage, register, welcome

app = webapp2.WSGIApplication([
    ('/?', blogfront.BlogFront),
    ('/signup', register.Register),
    ('/welcome', welcome.Welcome),
    ('/post/([0-9]+)', postpage.PostPage),
    ('/newpost', newpost.NewPost),
    ('/login', login.Login),
    ('/logout', logout.Logout),
    ('/edit/([0-9]+)', editpost.EditPost),
    ('/delete/([0-9]+)', deletepost.DeletePost),
    ('/newcomment/([0-9]+)', newcomment.NewComment),
    ('/editcomment/([0-9]+)/([0-9]+)', editcomment.EditComment),
    ('/deletecomment/([0-9]+)/([0-9]+)', deletecomment.DeleteComment),
    ('/like/([0-9]+)', likepost.LikePost),
    ],
    debug=True)
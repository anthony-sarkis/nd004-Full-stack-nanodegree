#!/usr/bin/env python
import os
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), "html")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    create = db.DateTimeProperty(auto_now_add = True)

class MainHandler(Handler):
    def render_front(self, title="", art="", error=""):
        self.render("front.html", title=title, art=art, error=error)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        #error handling
        #status 200 ok
        if title and art:
            #new instance of art
            a = Art(title = title, art = art)
            #store instance in db
            a.put()

            #rediect to avoid reload message 
            self.redirect("/")
            #self.write("thanks!")

        #error
        else:
            error = "we need both a title and some artwork!"
            #self.render("front.html", error = error)
            self.render_front(title, art, error)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)

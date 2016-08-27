#!/usr/bin/env python
import os
import webapp2
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), "html")
#template_dir = os.path.join(os.getcwd(), "html")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainHandler(Handler):
    def get(self):
        #self.response.out.write("Thanks!")
        self.render("shopping_list.html")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

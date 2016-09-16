#!/usr/bin/env python
import os
import webapp2
import jinja2
import re
from string import letters

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), "html")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

class Handler(webapp2.RequestHandler):
    # Create a template for "write" function
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    # Create a template for rending a string
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Rot13(Handler):
	""" Converts text into Ro13 """
	def get(self):
		# renders html form if get method is called
		self.render('rot13-form-custom.html')

	def post(self):
		Rot13 = ''
		text = self.request.get('text')
		# encode and decode text using built in rot13 functions 
		if text:
			rot13 = text.encode('rot13')

		# render HTML form and pass rot13 encoded text to text varilable
		self.render('rot13-form-custom.html', text = rot13)
		

app = webapp2.WSGIApplication([
    ('/', Rot13),
], debug=True)

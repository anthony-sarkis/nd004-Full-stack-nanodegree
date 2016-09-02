#!/usr/bin/env python
import os
import webapp2

form_html = """
    <form>
        <h2> Add a Food </h2>
        <input type="text" name="food">
        %s
        <button> Add </button>

    </form>
"""
hidden_html = """
    <input type="hidden" name="food" value="%s">
"""

item_html = "<li>%s</li>"

shopping_list_html = """
        <br>
        <br>
    <h2>Shopping List</h2>
        <ul>
        %s
        </ul>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        output = form_html
        output_hidden = ""

        items = self.request.get_all("food")
        if items:
            output_items = ""
            for item in items:
                output_hidden += hidden_html % item
                output_items += item_html % item

                output_shopping = shopping_list_html % output_items
                output += output_shopping

        output = output % output_hidden
        self.response.write(output)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

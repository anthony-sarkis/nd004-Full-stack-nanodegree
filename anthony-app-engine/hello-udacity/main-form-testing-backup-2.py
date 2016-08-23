#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

form="""
<form method="get" action="/">
  <label>
      pie
      <input type="radio" name="q" value = "one" > Male
  </label>
  apple <input type="radio" name="q" value = "two" checked> Female
  <input type="radio" name="q" value = "three" > Dog
  <br>
  <select name="q">
    <option value="lemon pie"> three </option>
    <option> two </option>
    </select>
  <input type="submit">
</form>
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
    def post(self):
        q = self.request.get("q")
        self.response.out.write(q)
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/testform', TestHandler)],
    debug=True)

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

def valid_day(day):
    if day.isdigit() is True:
        day = int(day)
        if day >= 1 and day <= 31:
            return day

import string
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

def valid_month(month):
    month = string.capitalize(month)
    if month in months:
        return month

def valid_year(year):
    if year.isdigit() is True:
        year = int(year)
        if 1900 <= year <= 2020:
            return year

form="""
<form method="post">
    What is your birthday?
    <br>

    <label>
      Day
      <input type="textbox" name="Day" value="%(day)s">
    </label>

    <label>
      Month
      <input type="textbox" name="Month" value="%(month)s">
    </label>

    <label>
      Year
      <input type="textbox" name="Year" value="%(year)s">
    </label>

    <div style="color: red">
    %(error)s
    </div>

    <br>
    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="", day="", month="", year=""):
        self.response.out.write(form % {"error": error,
                                        "day": day,
                                        "month": month,
                                        "year": year})
    def get(self):
        self.write_form()

    def post(self):
        user_day = self.request.get("Day")
        user_month = self.request.get("Month")
        user_year = self.request.get("Year")

        #so we can represent both Valid vars and what the user entered
        day = valid_day(user_day)
        month = valid_month(user_month)
        year = valid_year(user_year)

        if not (day and month and year):
            self.write_form("That doesn't look right",
                            user_day, user_month, user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', ThanksHandler)],
    debug=True)

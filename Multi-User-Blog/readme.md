
Documentation for Multi-User Blog
-------------
Release v0.2 October 2016


Files:
------------------------------------------------------------------------
Main entry and routes --> /main.py
Handlers --> /handlers
Models --> /models
Helper functions --> /helpers
HTML -> /html
CSS -> /css  (empty for now)


Description:
------------------------------------------------------------------------
The program generates a multi-user blog using Google App Engine db,
	webapp2, and jinja2. 

The primary functions are:
-> Secure user creation, login, and logout
-> Posting, viewing, editing and deleting text content.
-> Auxillary functions including commenting on posts, liking posts, etc.


Getting started:
------------------------------------------------------------------------
Live demo:
sarkis-blog.appspot.com

To run locally:
1. Install Google App Engine (GAE) SDK:
	https://cloud.google.com/appengine/downloads
2. Install Python 2.7
	https://www.python.org/downloads/
3. Unzip and open the "Blog-Project" folder
4. In GAE, add the root directory as an "Existing application".
5. Select the app and click run. Wait.
6. Click Browse. The application should open in your default browser.
	If not you can browse to the port shown. For example:
	http://localhost:10080/ where "10080" = Your_Port

Please note, even for the local version you must have an internet
	connection to download boot-strap (for css styling).

License:
------------------------------------------------------------------------

Portions from Udacity Full-Stack Engineer course and are copyright Udacity

Otherwise,

This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


Authors:
------------------------------------------------------------------------
Udacity
Anthony Sarkis


Contact:
------------------------------------------------------------------------
anthonysarkis@gmail.com



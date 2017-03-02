"""
12/22/2016

This project file is to is to learn and understand basic HTTP handling in python.

Place it in the /catalog folder to work with other files there.

"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations from Lesson 1
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                output = ""
                output += "<a href = '/restaurants/new' > Make a New Restaurant Here </a></br></br>"
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name

                    # Objective 2 -- Add Edit and Delete Links
                    output += "</br>"
                    output += "<a href='/restaurants/%s/edit'> Edit </a>" % restaurant.id

                    output += "</br>"
                    output += "<a href='/restaurants/%s/delete'> Delete </a>" % restaurant.id

                    output += "</br></br></br>"

                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Enter a new restaurant</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><h2>Name:</h2><input name="restaurant_name" type="text" ><input type="submit" value="Create"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                # split url on / , grab 3 item on 0 index
                restaurantIDPath = self.path.split("/")[2]

                # go to session, ask for restaurant, filter by the id from URL,
                # grab one record
                myRestaurantQuery = session.query(
                    Restaurant).filter_by(id=restaurantIDPath).one()

                # If query is not blank array
                if myRestaurantQuery != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>Edit %s</h1>" % myRestaurantQuery.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % restaurantIDPath
                    output += "<h2>Name:</h2><input name='restaurant_name' type='text' placeholder='%s'><input type='submit' value='Rename'>" % myRestaurantQuery.name
                    output += "</form></body></html>"
                    self.wfile.write(output)
                    return

            if self.path.endswith("/delete"):
                # split url on / , grab 3 item on 0 index
                restaurantIDPath = self.path.split("/")[2]

                # go to session, ask for restaurant, filter by the id from URL,
                # grab one record
                myRestaurantQuery = session.query(
                    Restaurant).filter_by(id=restaurantIDPath).one()

                # If query is not blank array
                if myRestaurantQuery != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>Delete %s</h1>" % myRestaurantQuery.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>" % restaurantIDPath
                    output += "<h2>Name:</h2><input name='restaurant_name' type='text' placeholder='%s'><input type='submit' value='Delete'>" % myRestaurantQuery.name
                    output += "</form></body></html>"
                    self.wfile.write(output)
                    return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    restaurant_name = fields.get('restaurant_name')

                    restaurant1 = Restaurant(name=restaurant_name[0])
                    session.add(restaurant1)
                    session.commit()

                    self.send_response(301)  # why here?
                    self.send_header('Content-type', 'text/html')
                    # redirect to homepage
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)

                    restaurant_name1 = fields.get('restaurant_name')
                    restaurantIDPath = self.path.split("/")[2]

                    # go to session, ask for restaurant, filter by the id from
                    # URL, grab one record
                    myRestaurantQuery = session.query(
                        Restaurant).filter_by(id=restaurantIDPath).one()

                    if myRestaurantQuery != []:
                        myRestaurantQuery.name = restaurant_name1[0]
                        # important when editing, you aren't adding a new object?
                        # instead we are calling the existing object, and name
                        # child, and re-declaring value?
                        session.add(myRestaurantQuery)
                        session.commit()

                        self.send_response(301)  # why here?
                        self.send_header('Content-type', 'text/html')
                        # redirect to homepage
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                # go to session, ask for restaurant, filter by the id from URL,
                # grab one record
                myRestaurantQuery = session.query(
                    Restaurant).filter_by(id=restaurantIDPath).one()

                if myRestaurantQuery:
                    # myRestaurantQuery.name = restaurant_name1[0]
                    # important when editing, you aren't adding a new object?
                    # instead we are calling the existing object, and name
                    # child, and re-declaring value?
                    session.delete(myRestaurantQuery)
                    session.commit()

                    self.send_response(301)  # why here?
                    self.send_header('Content-type', 'text/html')
                    # redirect to homepage
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        except:
            pass


def main():
    try:
        server = HTTPServer(('', 8080), webServerHandler)
        print 'Web server running...open localhost:8080/restaurants in your browser'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()

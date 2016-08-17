
import webbrowser

class Movie():
    def __init__(self, title, storyline, poster_img, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_img = poster_img
        self.trailer_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)

   

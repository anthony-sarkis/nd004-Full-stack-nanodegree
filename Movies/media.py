
import webbrowser

class Video():
    #Parent class
    def __init__(self, title):
        self.title = title

class TvShow(Video):
    #Child class
    def __init__(self, title): 
        Video.__init__(self, title)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

class Movie(Video):
    """ DOCS """
    valid_ratings = ["G", "PG", "R"]

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        Video.__init__(self, title)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)

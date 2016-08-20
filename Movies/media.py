
import webbrowser

class Video():
    """ Parent class """
    def __init__(self, title):
        """ Define parent class attributes """
        self.title = title

class TvShow(Video):
    """ Child class of Video """
    def __init__(self, title): 
        """ Define child class attributes, including inheriting title """
        
        Video.__init__(self, title)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

class Movie(Video):
    """ Child class of Video, Creates instance of Movie with attributes"""
    valid_ratings = ["G", "PG", "R"]
    
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        """ Define child class attributes including inheriting title """
        Video.__init__(self, title)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """ Calls the webbrowser function to show the trailer, references
        attributes defined in __init__
        """
        
        webbrowser.open(self.trailer_url)

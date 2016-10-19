from google.appengine.ext import db
from handlers import handler


class Comment(db.Model, handler.Handler):
    comment = db.TextProperty(required=True)
    author = db.IntegerProperty(required=True)

    def render(self):
        # Replace line break with html <br> to render well
        # call self to reference handler
        return self.render_str("comment.html", c=self)

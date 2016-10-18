from google.appengine.ext import db

class Comment(db.Model):
    comment = db.TextProperty(required=True)
    author = db.IntegerProperty(required=True)

    def render(Handler):
	        # Replace line break with html <br> to render well
	        return render_str("comment.html", c=self)
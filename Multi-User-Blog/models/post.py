from google.appengine.ext import db
from handlers import handler


class Post(db.Model, handler.Handler):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    # Used to assign a post to a user
    # TODO Consider using reference properties
    created_by = db.IntegerProperty(required=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    like = db.ListProperty(int)
    likes_count = db.IntegerProperty(default=0)

    def render(self):
        # Replace line break with html <br> to render well
        self.render_text = self.content.replace('\n', '<br>')
        return self.render_str("post.html", p=self)

    def renderNoButtons(self):
        # Replace line break with html <br> to render well
        self.render_text = self.content.replace('\n', '<br>')
        return self.render_str("post-no-buttons.html", p=self)

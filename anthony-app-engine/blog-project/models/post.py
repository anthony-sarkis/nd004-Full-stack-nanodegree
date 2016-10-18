from google.appengine.ext import db

class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    # Used to assign a post to a user
    created_by = db.IntegerProperty(required=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    like = db.ListProperty(int)
    likes_count = db.IntegerProperty(default=0)

    def renderNoButtons(Handler):
        # Replace line break with html <br> to render well
        self.render_text = self.content.replace('\n', '<br>')
        return render_str("post-no-buttons.html", p=self)
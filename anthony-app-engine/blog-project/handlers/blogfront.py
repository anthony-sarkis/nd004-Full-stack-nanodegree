from handlers import handler
from models import post, user

# render all posts blog front page
class BlogFront(handler.Handler):
    def get(self):
        # Get posts from DB. Select all from Post table order by created
        error = self.request.get("error")
        alert = self.request.get("alert")
        posts = post.Post.all().order('-created')
        # right way?
        if self.user:
            user_id = self.user.key().id()
        else:
            user_id = "notloggedin"
        # Render front page, pass "posts" variable as posts
        self.render('front.html', posts=posts, user_id=user_id, error=error, alert=alert)
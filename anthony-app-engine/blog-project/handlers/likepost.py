from handlers import handler
from google.appengine.ext import db
import time


class LikePost(handler.Handler):
    def get(self, post_id):
        if not self.user:
            error = "Please login to Like a post."
            self.redirect('/login?error=' + error)
        else:
            key = self.get_post_key(post_id)
            post = db.get(key)
            logged_user = self.user.key().id()
            created_by_actual = post.created_by

            if logged_user == created_by_actual:
                error = "Can't like your own post"
                self.redirect('/?error=' + error)
            elif logged_user in post.like:
                like = logged_user
                post.like.remove(like)
                post.likes_count -= 1
                post.put()
                time.sleep(200 / 1000)
                alert = "Unliked Post"
                self.redirect('/?alert=' + alert)
            else:
                like = logged_user
                post.like.append(like)
                post.likes_count += 1
                post.put()
                time.sleep(200 / 1000)
                alert = "Liked Post"
                self.redirect('/?alert=' + alert)

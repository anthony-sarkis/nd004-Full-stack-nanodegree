from handlers import handler
from handler import blog_key
from google.appengine.ext import db


class DeletePost(handler.Handler):
    def get(self, post_id):
        # Create key. Find post from post_id
        # Call int to transform string from URL into integer post ID
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        # Look up a specific item in the db using key
        post = db.get(key)
        # Return error if no valid key
        # !Important much come before content call
        if not post:
            self.error(404)
            return

        if self.user:
            # Now that we have the correct "post" we can call properties of it
            created_by_edit = self.getUserID()
            created_by_actual = post.created_by
            user_id = self.user.key().id()

            if created_by_actual == created_by_edit:
                self.render("deletepost.html", post=post, user_id=user_id)
                # TODO   Undo function?
                # Error handling if not valid user
                # TODO Redirect to login page, then redirect back automatically
            else:
                error = "Please login to delete"
                self.redirect('/login?error=' + error)
        else:
            error = "Please login to delete"
            self.redirect('/login?error=' + error)

    def post(self, post_id):
        # get from URL path the post key
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        # Permissions
        created_by_edit = self.getUserID()
        created_by_actual = post.created_by
        # If valid user, delete post and show success message
        if created_by_actual == created_by_edit:
            post.delete()
            alert = "Successfully deleted post"
            self.redirect('/?alert=' + alert)
        # Error handling if not valid user
        # TODO Redirect to login page, then redirect back automatically
        else:
            error = "Please login to delete"
            self.redirect('/login?error=' + error)

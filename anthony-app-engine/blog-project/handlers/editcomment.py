from handlers import handler
from google.appengine.ext import db
from models import comment
from handler import blog_key


class EditComment(handler.Handler):
    def get(self, post_id, comment_id):
        # Get post ID to link to commment
        post_key = self.get_post_key(post_id)
        post = db.get(post_key)
        if not post:
            self.error(404)
            return

        # Get comment key from second path
        comment_key = db.Key.from_path('Comment',
                                       int(comment_id), parent=post_key)
        the_comment = db.get(comment_key)
        # Access the comment itself from the comment class
        original_comment = the_comment.comment
        user_id = self.user.key().id()

        # Permissions, options could set here for editing
        if self.user and the_comment.author == user_id:
                self.render("editcomment.html", post=post,
                            comment=original_comment, user_id=user_id)
        else:
            error = "Please login to comment"
            self.redirect('/login?error=' + error)

    def post(self, post_id, comment_id):
        # Get variables passed from form
        updated_comment = self.request.get('comment')
        # assign post to a user using getUserbyID method
        author = self.getUserID()
        post_key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(post_key)

        comment_key = db.Key.from_path('Comment',
                                       int(comment_id), parent=post_key)
        old_comment_object = db.get(comment_key)
        old_comment = old_comment_object.comment

        # Permissions, options could set here for editing
        if self.user and old_comment_object.author == self.user.key().id():
            # Handle if valid post
            if updated_comment:
                # Create new post as p variable
                c = comment.Comment(key=comment_key, parent=post_key,
                                    comment=updated_comment, author=author)
                # Store element (p) in database
                c.put()
                # Redirect to blog page using ID of element
                self.redirect('/post/%s' % str(post.key().id()))

            # Error handling if invalid post
            else:
                # Define error message to user
                error = "Please write a comment"
                # Render HTML page with variables passed
                self.render("newcomment.html", post=post,
                            error=error, comment=old_comment)
        else:
            error = "Please login to comment"
            self.redirect('/login?error=' + error)

from handlers import handler
from google.appengine.ext import db
from models import comment


class NewComment(handler.Handler):
    def get(self, post_id):

        # Get post ID to link to commment
        post_key = self.get_post_key(post_id)
        post = db.get(post_key)
        if not post:
            self.error(404)
            return

        # Permissions, options could set here for editing
        if self.user:
                self.render("newcomment.html", post=post)
        else:
            error = "Please login to comment"
            self.redirect('/login?error=' + error)

    # On Post render
    def post(self, post_id):
        # Get variables passed from form
        the_comment = self.request.get('comment')
        # assign post to a user using getUserbyID method
        author = self.getUserID()
        post_key = self.get_post_key(post_id)
        post = db.get(post_key)

        # Handle if valid post
        if self.user:
            if the_comment:
                # Create new post as p variable
                c = comment.Comment(parent=post, comment=the_comment,
                                    author=author)
                # Store element (p) in database
                c.put()
                # Redirect to blog page using ID of element
                self.redirect('/post/%s' % str(post.key().id()))

            # Error handling if invalid post
            else:
                # Define error message to user
                error = "Please write a comment"
                # Render HTML page with variables passed
                self.render("newcomment.html", post=post, error=error,
                            comment=the_comment)
        else:
            error = "Please login to comment"
            self.redirect('/login?error=' + error)

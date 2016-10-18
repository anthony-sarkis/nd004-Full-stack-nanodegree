from handlers import handler

class EditComment(handler.Handler):
    def get(self, post_id, comment_id):
        # Get post ID to link to commment
        post_key = self.get_post_key(post_id)
        post = db.get(post_key)
        if not post:
            self.error(404)
            return

        # Get comment key from second path
        comment_key = db.Key.from_path('Comment', int(comment_id), parent=post_key)
        comment = db.get(comment_key)
        # Access the comment itself from the comment class
        original_comment = comment.comment

        # Permissions, options could set here for editing
        if self.user:
                self.render("editcomment.html", post=post, comment=original_comment)
        else:
            error = "Please login to comment"
            self.redirect('/login?error=' + error)

    def post(self, post_id, comment_id):
        # Get variables passed from form
        comment = self.request.get('comment')
        # assign post to a user using getUserbyID method
        author = self.getUserID()
        post_key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(post_key)

        comment_key = db.Key.from_path('Comment', int(comment_id), parent=post_key)

        # Handle if valid post
        if comment:
            # Create new post as p variable
            c = Comment(key=comment_key, parent=post_key, comment=comment,
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
            self.render("newcomment.html", post=post, error=error, comment=comment)
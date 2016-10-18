from handlers import handler

# Seems to be ok... but not sure if really happy with it.
class DeleteComment(handler.Handler):
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

        # Permissions
        created_by_edit = self.getUserID()
        created_by_actual = post.created_by
        # If valid user, delete post and show success message
        if created_by_actual == created_by_edit:
            comment.delete()
            #TODO Add success message
            self.redirect('/')
        # Error handling if not valid user
        # TODO Redirect to login page, then redirect back to delete page automatically
        else:
            error = "Please login to delete"
            self.redirect('/login?error=' + error)

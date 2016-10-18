from handlers import handler

# Render a specific post
class PostPage(handler.Handler):
    def get(self, post_id):
        key = self.get_post_key(post_id)
        # Look up a specific item in the db using key
        post = db.get(key)

        # working now!!! can use post or key?????
        comments = comment.Comment.all().ancestor(post)

        # Return error if no valid key
        if not post:
            self.error(404)
            return

        # Render page using Permalink HTML as a template, pass post var as post
        self.render("permalink.html", post=post, comments=comments)
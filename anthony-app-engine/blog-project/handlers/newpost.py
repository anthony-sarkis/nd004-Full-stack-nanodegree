from handlers import handler
from models import post


class NewPost(handler.Handler):
    """ """
    # Render new post HTML
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            error = "Please login to post"
            self.redirect('/login?error=' + error)

    # On Post render
    def post(self):
        # Get variables passed from form
        subject = self.request.get('subject')
        content = self.request.get('content')
        # assign post to a user using getUserbyID method
        created_by = self.getUserID()

        # Handle if valid post
        if subject and content:
            # Create new post as p variable
            p = post.Post(parent=blog_key(), subject=subject, content=content,
                     created_by=created_by, like=[])
            # Store element (p) in database
            p.put()
            # Redirect to blog page using ID of element
            self.redirect('/post/%s' % str(p.key().id()))

        # Error handling if invalid post
        else:
            # Define error message to user
            error = "Subject and Content please :)"
            # Render HTML page with variables passed
            self.render("newpost.html", subject=subject, content=content, error=error)

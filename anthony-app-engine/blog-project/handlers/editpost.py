from handlers import handler
from google.appengine.ext import db
from handler import blog_key


class EditPost(handler.Handler):
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
            # created_by_edit = self.getUserID()  What's the difference?
            created_by_edit = self.user.key().id()
            created_by_actual = post.created_by

            if created_by_actual == created_by_edit:
                # Now that we have the correct "post"
                # we can call properties of it

                content = post.content
                subject = post.subject

                # Render page using Permalink HTML as a template,
                # pass post var as post
                self.render("editpost.html", content=content, subject=subject, user_id=created_by_edit)
            else:
                error = "You don't have permission to edit this post. Please login as the user who created this post."
                # maybe hide button entierly?
                self.redirect('/?error=' + error)
        else:
            error = "Please login to edit"
            self.redirect('/login?error=' + error)

    def post(self, post_id):
        # Get variables passed from form
        subject = self.request.get('subject')
        content = self.request.get('content')
        # get from URL path the post key
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        # Check permissions. If same user trying to edit is who created it
        created_by_edit = self.getUserID()
        created_by_actual = post.created_by

        if created_by_actual == created_by_edit:
            # Handle if valid post
            if subject and content:
                # Update the post
                p = post.Post(key=key, parent=blog_key(), subject=subject,
                              content=content, created_by=created_by_actual)
                # Store element (p) in database
                p.put()
                # Redirect to blog page using ID of element
                self.redirect('/post/%s' % str(p.key().id()))

            # Error handling if invalid post
            else:
                # Define error message to user
                error = "Subject and Content please :)"
                # Render HTML page with variables passed
                self.render("editpost.html", subject=subject,
                            content=content, error=error)
        # Error handling if correct user is not logged in
        else:
            error = "You don't have permission to edit this post. Please login as the user who created this post."
            # maybe hide button entierly? error message is long
            self.redirect('/?error=' + error)

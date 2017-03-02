from handlers import handler


# Displays welcome page if valid user
class Welcome(handler.Handler):
    def get(self):
        if self.user:
            user_id = self.user.key().id()
            # Calling class function to look up username by name
            self.render('welcome.html', username=self.user.name, user_id=user_id)
        else:
            self.redirect('/signup')

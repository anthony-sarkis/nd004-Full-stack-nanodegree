from handlers import handler

# Displays welcome page if valid user
class Welcome(handler.Handler):
    def get(self):
        if self.user:
            # Calling class function to look up username by name
            self.render('welcome.html', username=self.user.name)
        else:
            self.redirect('/signup')
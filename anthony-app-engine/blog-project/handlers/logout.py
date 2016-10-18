from handlers import handler

# Logs out a user by clearing their cookies
class Logout(handler.Handler):
    def get(self):
        self.logout()
        self.redirect('/signup')
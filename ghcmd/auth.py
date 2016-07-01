import getpass
import base64

class Authorize:
    def __init__(self):
        self.username = input('Enter github username: ')
        self.auth_code = base64.b64encode(':'.join([
                        self.username,
                        getpass.getpass('password for {0}: '.format(self.username))
                        ]).encode('utf-8')
                    )

    def __repr__(self):
        return "Auth for github.com/{0}".format(self.username)

import requests
from socialize.helpers.auth_helpers import create_token_file, remove_token_file


class AuthService(object):

    def login(self, username, password):
        url = 'https://socialize.dmonn.ch/api/user/authorization/'
        r = requests.post(url, data={'username':username, 'password':password})
        if r.status_code == 200:
            status = create_token_file(r.json())
            print("Successfully logged in as "+ str(username))
        else:
            status = 403
            print("Unable to log in with given credentials.")
        return status

    def register(self, username, email, password):
        url = 'https://socialize.dmonn.ch/api/user/register/ '
        r = requests.post(url, data={'email': email, 'username':username, 'password':password})
        if r.status_code == 201:
            print("Successfully registered new user: "+ str(username) +".")
            self.login(username, password)
        else:
            print("Something went wrong, please contact the administrator or try another username.")

    def logout(self):
        remove_token_file()
        print("Successfully logged out.")


auth = AuthService()
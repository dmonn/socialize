import requests
from helpers.auth_helpers import create_token_file, remove_token_file


class AuthService(object):

    def login(self, username, password):
        url = 'https://socialize.dmonn.ch/api/user/authorization/'
        r = requests.post(url, data={'username':username, 'password':password})
        if r.status_code == 200:
            status = create_token_file(r.json())
        else:
            status = 403
        return status

    def register(self, username, email, password):
        url = 'https://socialize.dmonn.ch/api/user/register/ '
        r = requests.post(url, data={'email': email, 'username':username, 'password':password})
        if r.status_code == 201:
            self.login(username, password)
            return 200
        else:
            return 403

    def logout(self):
        remove_token_file()


auth = AuthService()
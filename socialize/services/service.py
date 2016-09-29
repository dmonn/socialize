import os.path
import requests
import sys

BASE_URL = 'https://socialize.dmonn.ch/api/'
# BASE_URL = 'http://localhost:8001/api/'


class Service(object):
    def get(self, path):
        if os.path.isfile(".AUTHTOKEN"):
            try:
                token = self.read_file(".AUTHTOKEN")
                r = requests.get(BASE_URL + path, headers={'Authorization': 'Token ' + token})
                return r.json()
            except Exception as e:
                print("An error occured. Send this to your administrator: " + str(e))
        else:
            return self.auth_failed()

    def post(self, path, data):
        if os.path.isfile(".AUTHTOKEN"):
            try:
                token = self.read_file(".AUTHTOKEN")
                r = requests.post(BASE_URL + path, headers={'Authorization': 'Token ' + token}, data=data)
                return r
            except Exception as e:
                print("An error occured. Send this to your administrator: " + str(e))
        else:
            return self.auth_failed()

    def auth_failed(self):
        """
        Do something if auth failed
        :return: Status and message
        """
        sys.exit("You aren't authenticated yet. Please use the login or register command to do so.")
        return(403, "Authentication failed")

    def read_file(self, filename):
        """
        Read a file with given filename
        :param filename: String
        :return: File content
        """
        with file(filename) as f:
            return f.read()

    def check_reponse(self, r, success,
                      error="There was an error with your request. Please use the --help function or contact the administrator."):
        if r.status_code == 200 and r.text != '400' and r.content != 403:
            print(str(success))
        else:
            print(str(error))

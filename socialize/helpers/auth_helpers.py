import os


def create_token_file(token):
    try:
        home_directory = os.path.expanduser('~')
        file = open(os.path.join(home_directory, ".AUTHTOKEN"), 'w')
        file.write(token['token'])
        file.close()
        return(200)
    except:
        print('Something went wrong!')


def remove_token_file():
    try:
        home_directory = os.path.expanduser('~')
        os.remove(os.path.join(home_directory, ".AUTHTOKEN"))
    except:
        print('Something went wrong!')

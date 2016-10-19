import os


def create_token_file(token):
    try:
        home_directory = os.environ['HOME']
        file = open(os.path.join(home_directory, ".AUTHTOKEN"), 'w')
        file.write(token['token'])
        file.close()
        return(200)
    except:
        print('Something went wrong!')


def remove_token_file():
    try:
        home_directory = os.environ['HOME']
        os.remove(os.path.join(home_directory, ".AUTHTOKEN"))
    except:
        print('Something went wrong!')

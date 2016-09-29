import os


def create_token_file(token):
    try:
        file = open(".AUTHTOKEN",'w')
        file.write(token['token'])
        file.close()
        return(200)
    except:
        print('Something went wrong!')


def remove_token_file():
    try:
        os.remove(".AUTHTOKEN")
    except:
        print('Something went wrong!')

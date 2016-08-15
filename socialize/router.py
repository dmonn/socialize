import click
from services.auth_service import auth

@click.group()
def init():
    """Official CLI client for 'Socialize - A social network on the cli'"""
    pass


@init.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
@click.option('--email', prompt=True)
def register(username, password, email):
    r = auth.register(username, email, password)
    if r == 200:
        print "Successfully registered new user: "+username+" and logged in."
    else:
        print "Something went wrong, please contact the administrator."


@init.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def login(username, password):
    r = auth.login(username, password)
    print password
    if r == 200:
        print "Successfully logged in as "+username
    else:
        print "Something went wrong, please contact the administrator."


@init.command()
def logout():
    auth.logout()

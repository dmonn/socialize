import click
from services.auth_service import auth
from services.user_service import user


@click.group()
def init():
    """Official CLI client for 'Socialize - A social network on the cli'"""
    pass

# AUTHENTICATION

@init.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
@click.option('--email', prompt=True)
def register(username, password, email):
    """Register a new user"""
    auth.register(username, email, password)


@init.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
def login(username, password):
    auth.login(username, password)


@init.command()
def logout():
    auth.logout()


# User Management

@init.command()
def me():
    """Shows current user"""
    user.get_current_user()
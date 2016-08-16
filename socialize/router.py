import click
from services.auth_service import auth
from services.user_service import usermanagement


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
    usermanagement.get_current_user()


@init.command()
@click.option('--slogan', help="Specify a slogan in quotes, e.g. 'this is my slogan'", default=None)
@click.option('--website', help="Specify a website", default=None)
@click.option('--interests', help="Specify some interests in quotes, e.g. 'Python, Stuff, Stuff'", default=None)
@click.option('--skills', help="Specify some skills in quotes, e.g. 'Programming, Eating, Sleeping'", default=None)
def profile(slogan, website, interests, skills):
    """Set profile details"""
    usermanagement.set_attr(slogan, website, interests, skills)


@init.command()
@click.argument('name')
def user(name):
    """Get a specific user by name"""
    usermanagement.get_user(name)


# Followingship

@init.command()
@click.argument('name')
def follow(name):
    """Follow a specific user"""
    usermanagement.follow_user(name)


@init.command()
@click.argument('name')
def unfollow(name):
    """Unfollow a specific user"""
    usermanagement.unfollow_user(name)

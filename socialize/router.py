import click
from services.auth_service import auth
from services.group_service import groups
from services.shoutout_service import shoutouts
from services.status_service import statusmanagement
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

# Status

@init.group()
def status():
    """Status management"""
    pass


@status.command()
def feed():
    """Get status feed of the 20 latest statuses"""
    statusmanagement.get_feed()

@status.command()
@click.argument('message')
def post(message):
    """Post a new status (use quotes)"""
    statusmanagement.post_status(message)


# Shoutouts

@init.group()
def shout():
    """Shoutout management"""
    pass


@shout.command()
def feed():
    """Get shout feed of the 20 latest shoutouts"""
    shoutouts.get_feed()

@shout.command()
@click.argument('message')
@click.option('--anon/--public', default=False)
def post(message, anon):
    """Post a new shoutout (use quotes). Use the anon option to post the shoutout anonymously"""
    shoutouts.post_status(message, anon)

# Groups

@init.group()
def group():
    """Group management"""
    pass


@group.command()
@click.argument('name')
@click.option('-p', '--password', default=None, help='Sometimes you have to provide a passphrase to join a group.')
def join(name, password):
    """Join a group with a given name (password might be to be provided"""
    groups.join_group(name, password)


@group.command()
@click.argument('name')
def leave(name):
    """Leave a previously joined group"""
    groups.leave_group(name)


@group.command()
@click.argument('name')
def delete(name):
    """Delete one of your groups (you have to be the creator!)"""
    groups.delete_group(name)


@group.command()
@click.argument('name')
def show(name):
    """Show group info"""
    groups.get_group(name)


@group.command()
@click.argument('name')
@click.option('-d', '--description', default=None, help='Set a short description of your group.')
@click.option('-p', '--password', default=None, help='Set your group to private and set a password.')
def create(name, description, password):
    """Create a new group with a given name You can also provide a short description and/or a password to make the group private"""
    groups.create_group(name, description, password)


# Groupmessages


@group.command()
@click.argument('name')
def feed(name):
    """Groupmessage feed"""
    groups.get_group_messages(name)


@group.command()
@click.argument('name')
@click.argument('message')
def message(name, message):
    """Post a new group message (write in quotes)"""
    groups.post_group_message(name, message)



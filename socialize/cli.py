import click

@click.group()
def init():
    """Official CLI client for 'Socialize - A social network on the cli'"""
    pass

@init.command()
@click.argument('username', nargs=1)
@click.argument('password', nargs=1)
def register(username, password):
    print("You choose: " +username+":"+password)

import requests
import click
from click.testing import CliRunner
from scripttest import TestFileEnvironment

# Verify installation

def test_message():
    @click.command()
    def cli():
        """Hello World!"""
        click.echo('I EXECUTED')

    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])

    assert not result.exception
    assert 'Hello World!' in result.output
    assert 'Show this message and exit.' in result.output
    assert result.exit_code == 0
    assert 'I EXECUTED' not in result.output

    result = runner.invoke(cli, [])
    assert not result.exception
    assert 'I EXECUTED' in result.output
    assert result.exit_code == 0


# Check Requests
def test_request_get():
    r = requests.get("https://google.com")
    assert r.status_code == 200

def test_request_post():
    r = requests.post('https://google.com', data={})
    assert r.status_code == 405


# Test Socialize Installation

def test_socialize():
    env = TestFileEnvironment('./test-output')
    env.reset()
    result = env.run('socl me')
    assert result.stdout.startswith("You aren't authenticated yet")

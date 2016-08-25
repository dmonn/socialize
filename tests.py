import click
import requests
from click.testing import CliRunner

from router import hack

def test_supporter_message():

    runner = CliRunner()
    result = runner.invoke(hack)

    assert result.exit_code == 0
    assert result.output == 'Find a teacher. Then kill your buddha.\n'


# Check Requests
def test_request_get():
    r = requests.get("https://google.com")
    assert r.status_code == 200

def test_request_post():
    r = requests.post('https://google.com', data={})
    assert r.status_code == 405
# pylint: disable=no-self-use

from .conftest import load

GITHUB_BASE = "http://github.com/jacebrowning/memegen/"


class TestRoot:

    def test_get_root(self, client):
        response = client.get("/api")

        assert 200 == response.status_code
        assert dict(
            templates="http://localhost/templates/",
            overview="http://localhost/overview",
            latest="http://localhost/latest",
            source=GITHUB_BASE,
            contributing=GITHUB_BASE + "blob/master/CONTRIBUTING.md",
        ) == load(response)

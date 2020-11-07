"""
This module allows querying NHL data using the statsapi.web.nhl.com API.

See the docs at https://gitlab.com/dword4/nhlapi/-/blob/master/stats-api.md
"""

import requests

BASE_URL = "https://statsapi.web.nhl.com"

# This header is used to tell the server that we need the results in a machine
# readable format. Otherwise we might get HTML that we'll have trouble reading.
DEFAULT_HEADERS = {"Accept": "application/json"}


def get_nhl_teams():
    """
    Get a list of NHL teams.

    .. code-block:: python

        {
            "teams": [
                {
                    "id": 1,
                    "name": "New Jersey Devils",
                    "link": "/api/v1/teams/1",
                    "venue": {
                        "name": "Prudential Center",
                        "link": "/api/v1/venues/null",
                        "city": "Newark",
                        "timeZone": {
                            "id": "America/New_York",
                            "offset": -5,
                            "tz": "EST"
                        }
                    },
                    "abbreviation": "NJD",
                    "teamName": "Devils",
                    "locationName": "New Jersey",
                    "firstYearOfPlay": "1982",
                    "division": {
                        "id": 18,
                        "name": "Metropolitan",
                        "nameShort": "Metro",
                        "link": "/api/v1/divisions/18",
                        "abbreviation": "M"
                    },
                    "conference": {
                        "id": 6,
                        "name": "Eastern",
                        "link": "/api/v1/conferences/6"
                    },
                    "franchise": {
                        "franchiseId": 23,
                        "teamName": "Devils",
                        "link": "/api/v1/franchises/23"
                    },
                    "shortName": "New Jersey",
                    "officialSiteUrl": "http://www.newjerseydevils.com/",
                    "franchiseId": 23,
                    "active": true
                },
            ]

    Returns:
        The data for all NHL teams.
    """

    # First thing we'll do is format the URL for this endpoint
    url = f"{BASE_URL}/api/v1/teams"

    # Call the API with the correct headers
    res = requests.get(url=url, headers=DEFAULT_HEADERS)

    # Check that the response has no errors in it first
    res.raise_for_status()

    # This helper method turns the response into a simple python object.
    return res.json()


def get_nhl_team_names():
    """
    Get the name of every NHL team.

    Returns:
        a list of team names.
    """

    # Get the data using the API we already wrote
    data = get_nhl_teams()

    # Use a list comprehension to parse the results!
    # See https://www.programiz.com/python-programming/list-comprehension
    return [team["name"] for team in data["teams"]]

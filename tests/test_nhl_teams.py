from sportsdata.nhl import get_nhl_team_names
from sportsdata.scripts import print_nhl_teams


def test_get_nhl_team_names(requests_mock):
    """
    Test that the get_nhl_team_names method parses out names as we expect.
    """

    requests_mock.get(
        "https://statsapi.web.nhl.com/api/v1/teams",
        json={
            "teams": [
                {"name": "foo"},
                {"name": "bar"},
            ]
        },
    )

    assert get_nhl_team_names() == ["foo", "bar"]


def test_print_nhl_team(requests_mock, capsys):
    """
    Test that the print-nhl-teams main method prints what we expect.
    """

    requests_mock.get(
        "https://statsapi.web.nhl.com/api/v1/teams",
        json={
            "teams": [
                {"name": "foo"},
                {"name": "bar"},
            ]
        },
    )

    print_nhl_teams.main()
    captured = capsys.readouterr()
    assert captured.out == "foo\nbar\n"

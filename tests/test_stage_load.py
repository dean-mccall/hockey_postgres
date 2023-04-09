"""test cases"""
# import hockey_load.stage_model
from hockey_load.stage_load import team_from_dict
from hockey_load.stage_load import load_teams


def test_team_from_dict():
    """test_team_from_dict"""
    source = {
        'team_url': 'http://test/test',
        'league_conference': 'test conference',
        'conference_division': 'test division',
        'team_name': 'test team'
    }

    team = team_from_dict(source)

    # check value mapping
    assert team.team_url, source['team_url']
    assert team.team_name, source['team_name']
    assert team.league_conference, source['league_conference']
    assert team.conference_division, source['conference_division']


def test_load_teams():
    """test_load_teams"""
    load_teams('/Users/dean.mccall/tmp/json/team')

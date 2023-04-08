"""test cases"""
# import hockey_load.stage_model
from hockey_load.stage_load import team_from_dictionary


def test_team_from_dictionary():
    source = {
        'team_url': 'http://test/test',
        'conference': 'test conference',
        'conference_division': 'test division',
        'team': 'test team'
    }

    team = team_from_dictionary(source)

    # check value mapping
    assert team.team_url, source['team_url']
    assert team.team, source['team']

"""test cases"""
# import hockey_load.stage_model
from sqlalchemy import func
from sqlalchemy.orm import Session

from hockey_load.wikipedia_load import (load_career_statistics, load_players,
                                    load_teams, player_from_dict,
                                    team_from_dict)
from hockey_load.wikipedia_model import CareerStatistic, Player, Team, get_engine

EXPECTED_TEAM_COUNT = 32
MINIMUM_PLAYER_COUNT = 800


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

    with Session(get_engine()) as session:
        with session.begin():
            row_count = session.query(Team).count()
            assert row_count == EXPECTED_TEAM_COUNT



def test_player_from_dict():
    """test_player_from_dict"""
    source = {
        "player_name": "Aaron Ekblad",
        "player_url": "https://en.wikipedia.org/wiki/Aaron_Ekblad",
        "born": "1996-02-07 00:00:00",
        "height": 193,
        "weight": 100,
        "position": "Defence",
        "shoots": "Right",
        "nhl_team": "Florida Panthers",
        "national_team": "\u00a0Canada",
        "nhl_draft": "1st overall, 2014Florida Panthers",
        "playing_career": "2014-present"
    }

    player = player_from_dict(source)
    assert player.player_name == source['player_name']
    assert player.player_url == source['player_url']
    assert player.born == source['born']
    assert player.height == source['height']
    assert player.weight == source['weight']
    assert player.position == source['position']
    assert player.shoots == source['shoots']
    assert player.nhl_team == source['nhl_team']
    assert player.national_team == source['national_team']
    assert player.nhl_draft == source['nhl_draft']
    assert player.playing_career == source['playing_career']


def test_load_players():
    """test_load_players"""
    load_players('/Users/dean.mccall/tmp/json/player')

    with Session(get_engine()) as session:
        with session.begin():
            row_count = session.query(Player).count()
            assert row_count >= MINIMUM_PLAYER_COUNT


def test_load_career_statistics():
    """test_load_career_statistics"""
    load_career_statistics('/Users/dean.mccall/tmp/json/player')

    with Session(get_engine()) as session:
        with session.begin():
            row_count = session.query(CareerStatistic).count()
            assert row_count >= MINIMUM_PLAYER_COUNT


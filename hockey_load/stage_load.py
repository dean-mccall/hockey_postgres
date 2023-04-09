"""stage_load"""
import json
import logging
from pathlib import Path

from sqlalchemy.orm import Session

from hockey_load.stage_model import Player, Team, get_engine

#  configure logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s | %(name)s | %(levelname)s | %(message)s')










def team_from_dict(source: dict) -> Team:
    """translate dictionary insert"""
    logging.debug('mapping dictionary to columns')

    return Team(
        team_url = source.get('team_url'),
        league_conference = source.get('league_conference'),
        conference_division = source.get('conference_division'),
        team_name = source.get('team_name')
    )



def load_teams(input_folder_name:str):
    """load_teams"""
    logging.debug('loading files from %s', input_folder_name)


    with Session(get_engine()) as session:
        with session.begin():
            row_count = session.query(Team).delete()
            logging.info('removed %s teams', row_count)

        input_folder = Path(input_folder_name)
        with session.begin():
            team_count = 0
            for team_file in input_folder.iterdir():
                team_count = team_count + 1
                with open(team_file, encoding = 'utf8') as team_json_file:
                    source_team = json.load(team_json_file)
                    target_team = team_from_dict(source_team)
                    session.add(target_team)

            logging.info('loaded %s teams', team_count)


def load_players(input_folder_name:str):
    """load_players"""
    logging.debug('loaded players from %s, input_folder_name')

    with Session(get_engine()) as session:
        with session.begin():
            row_count = session.query(Player).delete()
            logging.info('removed %s players', row_count)


        input_folder = Path(input_folder_name)
        with session.begin():
            player_count = 0
            for player_file in input_folder.iterdir():
                player_count = player_count + 1
                with open(player_file, encoding = 'utf-8') as player_json_file:
                    source_player = json.load(player_json_file)
                    target_player = player_from_dict(source_player)
                    session.add(target_player)

            logging.info('loaded %s players', player_count)




def player_from_dict(source:dict):
    """player_from_dict"""
    return Player(
        source.get('player_name'),
        source.get('player_url'),
        source.get('born'),
        source.get('height'),
        source.get('weight'),
        source.get('position'),
        source.get('shoots'),
        source.get('nhl_team'),
        source.get('national_team'),
        source.get('nhl_draft'),
        source.get('playing_career'))




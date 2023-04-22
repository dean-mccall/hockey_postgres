"""stage_load"""
import json
import logging
from pathlib import Path

from sqlalchemy.orm import Session

from hockey_load.wikipedia_model import CareerStatistic, Player, Team, get_engine

#  configure logging
logger = logging.getLogger(__name__)



def team_from_dict(source: dict) -> Team:
    """translate dictionary insert"""
    return Team(
        team_url = source.get('team_url'),
        league_conference = source.get('league_conference'),
        conference_division = source.get('conference_division'),
        team_name = source.get('team_name')
    )



def load_teams(input_folder_name:str):
    """load_teams"""
    logger.debug('loading files from %s', input_folder_name)


    with Session(get_engine()) as session:
        with session.begin():
            row_count = session.query(Team).delete()
            logger.info('removed %s teams', row_count)

        input_folder = Path(input_folder_name)
        with session.begin():
            team_count = 0
            for team_file in input_folder.iterdir():
                team_count = team_count + 1
                with open(team_file, encoding = 'utf8') as team_json_file:
                    source_team = json.load(team_json_file)
                    target_team = team_from_dict(source_team)
                    session.add(target_team)

            logger.info('loaded %s teams', team_count)


def load_players(input_folder_name:str):
    """load_players"""
    logger.debug('loaded players from %s, input_folder_name')

    with Session(get_engine()) as session:
        with session.begin():
            row_count = session.query(Player).delete()
            logger.info('removed %s players', row_count)


        input_folder = Path(input_folder_name)
        with session.begin():
            player_count = 0
            for player_file in input_folder.iterdir():
                player_count = player_count + 1
                with open(player_file, encoding = 'utf-8') as player_json_file:
                    source_player = json.load(player_json_file)
                    target_player = player_from_dict(source_player)
                    session.add(target_player)

            logger.info('loaded %s players', player_count)




def player_from_dict(source:dict):
    """player_from_dict"""
    return Player(
        player_name = source.get('player_name'),
        player_url = source.get('player_url'),
        born = source.get('born'),
        height = source.get('height'),
        weight = source.get('weight'),
        position = source.get('position'),
        shoots = source.get('shoots'),
        nhl_team = source.get('nhl_team'),
        national_team = source.get('national_team'),
        nhl_draft = source.get('nhl_draft'),
        playing_career = source.get('playing_career'))



def career_statistic_from_dict(source:dict):
    result = CareerStatistic()
    result.player_url = source.get('player_url')
    result.season = source.get('season')
    result.team = source.get('team')
    result.league = source.get('league')
    result.regular_season_games_played_count = source.get('regular_season_games_played_count')
    result.regular_season_goal_count = source.get('regular_season_goal_count')
    result.regular_season_assist_count = source.get('regular_season_assist_count')
    result.regular_season_point_count = source.get('regular_season_point_count')
    result.regular_season_penalty_minute_count = source.get('regular_season_penalty_minute_count')
    result.playoff_season_games_played_count = source.get('playoff_season_games_played_count')
    result.playoff_season_goal_count = source.get('playoff_season_goal_count')
    result.playoff_season_assist_count = source.get('playoff_season_assist_count')
    result.playoff_season_point_count = source.get('playoff_season_point_count')
    result.playoff_season_penalty_minute_count = source.get('playoff_season_penalty_minute_count')

    return result


def load_career_statistics(input_folder_name:str):
    logger.debug('loading players from %s', input_folder_name)

    with Session(get_engine()) as session:
        with session.begin():
            row_count = session.query(CareerStatistic).delete()
            logger.info('removed %s career statistics', row_count)

        input_folder = Path(input_folder_name)
        with session.begin():
            career_statistic_count = 0
            for player_file in input_folder.iterdir():
                with open(player_file, encoding = 'utf-8') as player_json_file:
                    source_player = json.load(player_json_file)
                    if 'career_statistics' in source_player:
                        for source_career_statistic in source_player['career_statistics']:
                            career_statistic_count = career_statistic_count + 1
                            source_career_statistic['player_url'] = source_player['player_url']
                            target_career_statistic = career_statistic_from_dict(source_career_statistic)
                            session.add(target_career_statistic)


            logger.info('loaded %s career_statistics', career_statistic_count)

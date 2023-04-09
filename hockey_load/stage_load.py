"""stage_load"""
import logging
from pathlib import Path
import json

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from hockey_load.stage_model import get_engine
from hockey_load.stage_model import Team

#  configure logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s | %(name)s | %(levelname)s | %(message)s')










def team_from_dict(source: dict) -> Team:
    """translate dictionary insert"""
    logging.debug('mapping dictionary to columns')

    return Team(
        team_url = source['team_url'],
        league_conference = source['league_conference'],
        conference_division = source['conference_division'],
        team_name = source['team_name']
    )



def load_teams(input_folder_name:str):
    """load_teams"""
    logging.debug('loading files from {input_folder_name}')


    Session = sessionmaker(bind = get_engine())
    session = Session()


    input_folder = Path(input_folder_name)
    for team_file in input_folder.iterdir():
        with open(team_file, encoding = 'utf8') as team_json_file:
            source_team = json.load(team_json_file)
            target_team = team_from_dict(source_team)
            session.add(target_team)

    session.commit()
    session.close()







def orm_create_team(session: Session, team: Team):
    """orm_create_team"""
    try:
        session.add(team)
        session.commit()
    except SQLAlchemyError as sql_error:
        logging.error('Unexpected error when creating user: {sql_error}')
        raise sql_error


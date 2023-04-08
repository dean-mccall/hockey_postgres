"""stage_load"""
import logging
from hockey_load.stage_model import Team
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


#  configure logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s | %(name)s | %(levelname)s | %(message)s')










def team_from_dictionary(source: dict) -> Team:
    """translate dictionary insert"""
    logging.debug('mapping dictionary to columns')

    return Team(
        team_url = source['team_url'],
        conference = source['conference'],
        conference_division = source['conference_division'],
        team = source['team']
    )



def orm_create_team(session: Session, team: Team):
    """orm_create_team"""
    try:
        session.add(team)
        session.commit()
    except SQLAlchemyError as sql_error:
        logging.error('Unexpected error when creating user: {sql_error}')
        raise sql_error
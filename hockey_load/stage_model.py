"""Declare models and relationships."""
import logging
from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database, drop_database


Base = declarative_base()
#  configure logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s | %(name)s | %(levelname)s | %(message)s')



class Player(Base):
    """player"""

    __tablename__ = 'player'

    player_name = Column(String(255), nullable = True)
    player_url = Column(String(255), nullable = True, primary_key = True)
    born = Column(String(255), nullable = True)
    height = Column(String(255), nullable = True)
    weight = Column(String(255), nullable = True)
    position = Column(String(255), nullable = True)
    shoots = Column(String(255), nullable = True)
    nhl_team = Column(String(255), nullable = True)
    national_team = Column(String(255), nullable = True)
    nhl_draft = Column(String(255), nullable = True)
    playing_career = Column(String(255), nullable = True)



class Team(Base):
    """team"""

    __tablename__ = 'team'

    team_url = Column(String(255), nullable = True, primary_key = True)
    conference = Column(String(255), nullable = True)
    conference_division = Column(String(255), nullable = True)
    team = Column(String(255), nullable = True)


    def __init__(self, team_url:str, conference:str, conference_division:str, team:str):
        self.team_url = team_url
        self.conference = conference
        self.conference_division = conference_division
        self.team = team


class CareerStatistic(Base):
    """career_statistic"""

    __tablename__ = 'career_statistic'

    player_url = Column(String(255), nullable = True, primary_key = True)
    season = Column(String(255), nullable = True)
    team = Column(String(255), nullable = True)
    league = Column(String(255), nullable = True)
    regular_season_games_played_count = Column(String(255), nullable = True)
    regular_season_goal_count = Column(String(255), nullable = True)
    regular_season_assist_count = Column(String(255), nullable = True)
    regular_season_point_count = Column(String(255), nullable = True)
    regular_season_penalty_minute_count = Column(String(255), nullable = True)
    playoff_season_games_played_count = Column(String(255), nullable = True)
    playoff_season_goal_count = Column(String(255), nullable = True)
    playoff_season_assist_count = Column(String(255), nullable = True)
    playoff_season_point_count = Column(String(255), nullable = True)
    playoff_season_penalty_minute_count = Column(String(255), nullable = True)



def get_engine():
    """getEngine"""
    return create_engine('postgresql://localhost/hockey')


def deploy_schema():
    """deploy schema"""
    engine = get_engine()
    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(engine)

    logging.debug('deploy_schema done')

def undeploy_schema():
    """undeploy schema"""
    engine = get_engine()
    if database_exists(engine.url):
        drop_database(engine.url)


def restart_schema():
    """drop and recreate"""
    undeploy_schema()
    deploy_schema()
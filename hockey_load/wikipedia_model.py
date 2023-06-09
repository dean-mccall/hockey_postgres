"""Declare models and relationships."""
import logging

from sqlalchemy import Column, String, Integer, Identity, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists, drop_database
from sqlalchemy import MetaData
from sqlalchemy.schema import CreateSchema
from sqlalchemy.sql import text
from sqlalchemy.exc import ProgrammingError

logger = logging.getLogger(__name__)

SCHEMA_NAME = 'wikipedia'
metadata = MetaData(schema = SCHEMA_NAME)
Base = declarative_base(metadata = metadata)


class Player(Base):
    """player"""

    __tablename__ = 'players'

    player_id = Column(Integer, Identity(), primary_key = True)
    player_name = Column(String(255), nullable = True)
    player_url = Column(String(255), nullable = True)
    born = Column(String(255), nullable = True)
    height = Column(String(255), nullable = True)
    weight = Column(String(255), nullable = True)
    position = Column(String(255), nullable = True)
    shoots = Column(String(255), nullable = True)
    nhl_team = Column(String(255), nullable = True)
    national_team = Column(String(255), nullable = True)
    nhl_draft = Column(String(255), nullable = True)
    playing_career = Column(String(255), nullable = True)

    def __init__(
            self,
            player_name,
            player_url,
            born,
            height,
            weight,
            position,
            shoots,
            nhl_team,
            national_team,
            nhl_draft,
            playing_career):
        self.player_name = player_name
        self.player_url = player_url
        self.born = born
        self.height = height
        self.weight = weight
        self.position = position
        self.shoots = shoots
        self.nhl_team = nhl_team
        self.national_team = national_team
        self.nhl_draft = nhl_draft
        self.playing_career = playing_career





class Team(Base):
    """team"""

    __tablename__ = 'teams'

    team_id = Column(Integer, Identity(), primary_key = True)
    team_url = Column(String(255), nullable = True)
    league_conference = Column(String(255), nullable = True)
    conference_division = Column(String(255), nullable = True)
    team_name = Column(String(255), nullable = True)


    def __init__(self, team_url:str, league_conference:str, conference_division:str, team_name:str):
        self.team_url = team_url
        self.league_conference = league_conference
        self.conference_division = conference_division
        self.team_name = team_name


class CareerStatistic(Base):
    """career_statistics"""

    __tablename__ = 'career_statistics'

    career_statistic_id = Column(Integer, Identity(), primary_key = True)
    player_url = Column(String(255), nullable = True)
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

    def __init__(
        self,
        player_url:str,
        season:str,
        team:str,
        league:str,
        regular_season_games_played_count:str,
        regular_season_goal_count:str,
        regular_season_assist_count:str,
        regular_season_point_count:str,
        regular_season_penalty_minute_count:str,
        playoff_season_games_played_count:str,
        playoff_season_goal_count:str,
        playoff_season_assist_count:str,
        playoff_season_point_count:str,
        playoff_season_penalty_minute_count:str):

        self.player_url = player_url
        self.season = season
        self.team = team
        self.league = league
        self.regular_season_games_played_count = regular_season_games_played_count
        self.regular_season_goal_count = regular_season_goal_count
        self.regular_season_assist_count = regular_season_assist_count
        self.regular_season_point_count = regular_season_point_count
        self.regular_season_penalty_minute_count = regular_season_penalty_minute_count
        self.playoff_season_games_played_count = playoff_season_games_played_count
        self.playoff_season_goal_count = playoff_season_goal_count
        self.playoff_season_assist_count = playoff_season_assist_count
        self.playoff_season_point_count = playoff_season_point_count
        self.playoff_season_penalty_minute_count = playoff_season_penalty_minute_count

    def __init__(self):
        pass



def get_engine():
    """getEngine"""
    return create_engine('postgresql://localhost/hockey')


def deploy_schema():
    """deploy schema"""
    engine = get_engine()

    if not database_exists(engine.url):
        create_database(engine.url)
        with engine.connect() as connection:
            with connection.begin():
                connection.execute(CreateSchema(SCHEMA_NAME))

            #  create database roles
            with connection.begin():
                try:
                    connection.execute(text('CREATE ROLE hockey_ro'))
                except ProgrammingError as e:
                    #  swallow this error.  the object exists
                    pass

            with connection.begin():
                try:
                    connection.execute(text('CREATE ROLE hockey_rw'))
                except ProgrammingError as e:
                    #  swallow this error.  the object exists
                    pass

            with connection.begin():
                connection.execute(text(f'GRANT USAGE ON SCHEMA {SCHEMA_NAME} TO hockey_ro'))
                connection.execute(text(f'GRANT USAGE ON SCHEMA {SCHEMA_NAME} TO hockey_ro'))


    Base.metadata.create_all(engine)


    #  grant permissions to the roles
    with engine.connect() as connection:
        with connection.begin():
            connection.execute(text(f'GRANT SELECT ON ALL TABLES IN SCHEMA {SCHEMA_NAME} TO hockey_ro'))
            connection.execute(text(f'GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA {SCHEMA_NAME} TO hockey_rw'))


    logger.info('schema deployed')

def undeploy_schema():
    """undeploy schema"""
    engine = get_engine()
    if database_exists(engine.url):
        drop_database(engine.url)
    logger.info('schema undeployed')


def redeploy_schema():
    """drop and recreate"""
    undeploy_schema()
    deploy_schema()



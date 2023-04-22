WITH cleaned_career_statistics AS
(
    SELECT
        career_statistic_id,
        LOWER(player_url) player_url,
        season,
        CAST(REGEXP_REPLACE(team, '[\u000a]', '', 'g') AS VARCHAR(255)) team,
        UPPER(league) league,
        CAST(regular_season_games_played_count AS INTEGER) regular_season_games_played_count,
        CAST(regular_season_goal_count AS INTEGER) regular_season_goal_count,
        CAST(regular_season_assist_count AS INTEGER) regular_season_assist_count,
        CAST(regular_season_point_count AS INTEGER) regular_season_point_count,
        CAST(regular_season_penalty_minute_count AS INTEGER) regular_season_penalty_minute_count,
        CAST(playoff_season_games_played_count AS INTEGER) playoff_season_games_played_count,
        CAST(playoff_season_goal_count AS INTEGER) playoff_season_goal_count,
        CAST(playoff_season_assist_count AS INTEGER) playoff_season_assist_count,
        CAST(playoff_season_point_count AS INTEGER) playoff_season_point_count,
        CAST(playoff_season_penalty_minute_count AS INTEGER) playoff_season_penalty_minute_count
    FROM {{ source('wikipedia','career_statistics') }}
)
SELECT *
FROM cleaned_career_statistics


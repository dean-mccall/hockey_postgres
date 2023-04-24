SELECT * FROM wikipedia.players;

WITH cleaned_players AS
(
    SELECT 
        player_id,
        player_name,
        player_url,
        CAST(born AS DATE) born,
        CAST(height AS INTEGER) height_centimeters,
        ROUND((CAST(height AS INTEGER) * .393701), 2) height_inches,
        TRUNC(CAST(height AS INTEGER) * .393701 / 12) height_feet,
        CAST(TRUNC((CAST(height AS INTEGER) * .393701) / 12) AS VARCHAR)||' feet '||CAST(ROUND(((((CAST(height AS INTEGER) * .393701) / 12) - TRUNC((CAST(height AS INTEGER) * .393701) / 12))) * 12, 0) AS VARCHAR)||' inches' height_feet_and_inches, 
        CAST(weight AS INTEGER) weight_kilograms,
        ROUND(CAST(weight AS INTEGER) * 2.20462, 0) weight_pounds,
        position,
        shoots,
        national_team,
        nhl_draft,
        CASE 
            WHEN LENGTH(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(SPLIT_PART(nhl_draft, ',', 1), 'th overall', ''), 'rd overall', ''), 'nd overall', ''), 'Undrafted', ''), 'st overall', '')) = 0 THEN NULL
            ELSE CAST(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(SPLIT_PART(nhl_draft, ',', 1), 'th overall', ''), 'rd overall', ''), 'nd overall', ''), 'Undrafted', ''), 'st overall', '') AS INTEGER)
        END nhl_draft_position,
        CASE    
            WHEN LENGTH(SUBSTR(SPLIT_PART(nhl_draft, ',', 2), 1, 5)) = 0 THEN NULL
            ELSE CAST(SUBSTR(SPLIT_PART(nhl_draft, ',', 2), 1, 5) AS INTEGER)
        END nhl_draft_year,
        CASE
            WHEN LENGTH(SUBSTR(SPLIT_PART(nhl_draft, ',', 2), 6, LENGTH(nhl_draft))) = 0 THEN NULL
            ELSE CAST(SUBSTR(SPLIT_PART(nhl_draft, ',', 2), 6, LENGTH(nhl_draft)) AS VARCHAR(255))
        END nhl_draft_team,
        playing_career,
        CASE
            WHEN LENGTH(SPLIT_PART(REPLACE(playing_career, 'TBD', ''), '-', 1)) = 0 THEN NULL
            ELSE CAST(SPLIT_PART(REPLACE(playing_career, 'TBD', ''), '-', 1) AS INTEGER) 
        END playing_career_start_year,
        CASE
            WHEN SPLIT_PART(REPLACE(playing_career, 'TBD', ''), '-', 2) = 'present' THEN NULL
            ELSE CAST(SPLIT_PART(REPLACE(playing_career, 'TBD', ''), '-', 2) AS INTEGER)
        END player_career_end_year
    FROM wikipedia.players
)
SELECT *
FROM cleaned_players

SELECT *
FROM stg_wikipedia__players

SELECT 180 centimeters, 180 * .393701 inches, TRUNC((180 * .393701) / 12) feet, ROUND(((((180 * .393701) / 12) - TRUNC((180 * .393701) / 12))) * 12, 0)

SELECT COALESCE('1', NULL)

SELECT CAST(TRUNC((CAST(height AS INTEGER) * .393701) / 12) AS VARCHAR)||' feet '||CAST(ROUND(((((CAST(height AS INTEGER) * .393701) / 12) - TRUNC((CAST(height AS INTEGER) * .393701) / 12))) * 12, 0) AS VARCHAR)||' inches'
FROM wikipedia.players

SELECT *
FROM wikpedia.career_statistics

WITH cleaned_career_statistics AS
(
    SELECT 
        career_statistic_id,
        player_url,
        season,
        CAST(REGEXP_REPLACE(team, '[\u000a]', '', 'g') AS VARCHAR(255)) team,
        league,
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
    FROM wikipedia.career_statistics
)
SELECT *
FROM cleaned_career_statistics



SELECT COUNT(*) FROM (SELECT league, COUNT(*)
FROM public.stg_wikipedia__career_statistics
GROUP BY league
ORDER BY COUNT(*) DESC) x

SELECT *
FROM stg_wikipedia__career_statistics
WHERE player_url = 'https://en.wikipedia.org/wiki/nathan_mackinnon'
ORDER BY season ASC

SELECT
    player_url,
    league,
    MIN(season) rookie_season,
    MIN(career_statistic_id) rookie_season_career_statistic_id
FROM stg_wikipedia__career_statistics
WHERE player_url = 'https://en.wikipedia.org/wiki/nathan_mackinnon'
GROUP BY
    player_url,
    league

SELECT * FROM public.int_players_rookie_season

SELECT * FROM public.stg_wikipedia__career_statistics

SELECT *
FROM public.int_players_rookie_season
ORDER BY player_url, league, rookie_season

SELECT *
FROM public.fact_career_statistics
WHERE rookie_season_indicator = 'Y'
ORDER BY player_url, season

SELECT team, league, season, rookie_season_indicator, rookie_nhl_season_indicator, pre_nhl_season_indicator
FROM fact_career_statistics
WHERE player_url = LOWER('https://en.wikipedia.org/wiki/Andrew_Cogliano')
AND rookie_season_indicator = 'Y'
AND (pre_nhl_season_indicator = 'Y'
OR rookie_nhl_season_indicator = 'Y')
ORDER BY season

SELECT 
    'WHEN league = '''||league||''' THEN '
FROM dim_leagues
ORDER BY league ASC

SELECT *
FROM stg_wikipedia__career_statistics
WHERE league = 'ALLSV'

SELECT *
FROM stg_wikipedia__players
WHERE player_url = 'https://en.wikipedia.org/wiki/Thomas_Greiss'

SELECT *
fROM public.tier

SELECT * FROM public.league_tier

SELECT * FROM int_player_rookie_tier_seasons
WHERE player_url = 'https://en.wikipedia.org/wiki/Nathan_MacKinnon'

SELECT * FROM dim_leagues

SELECT *
FROM int_player_rookie_tier_seasons

SELECT 
    fcs.season,
    fcs.team,
    fcs.league,
    dl.tier,
    fcs.rookie_league_season_indicator,
    fcs.rookie_nhl_season_indicator,
    fcs.pre_nhl_season_indicator,
    fcs.rookie_tier_season_indicator
FROM fact_career_statistics fcs
INNER JOIN dim_leagues dl 
    ON fcs.league = dl.league
WHERE fcs.player_url = 'https://en.wikipedia.org/wiki/Nathan_MacKinnon'
AND fcs.rookie_tier_season_indicator = 'Y'

SELECT COUNT(*) FROM stg_wikipedia__career_statistics

SELECT COUNT(*) FROM fact_career_statistics

SELECT * FROM dim_leagues

WITH leagues AS
(
    SELECT DISTINCT league
    FROM stg_wikipedia__career_statistics
),
league_tiers AS
(
    SELECT *
    FROM league_tiers
),
final AS
(
    SELECT 
        leagues.league,
        league_tiers.tier
    FROM leagues
    LEFT OUTER JOIN league_tiers
        ON leagues.league = league_tiers.league
)
SELECT *
FROM final
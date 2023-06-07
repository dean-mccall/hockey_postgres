WITH career_statistics AS
(
    SELECT *
    FROM {{  ref('stg_wikipedia__career_statistics') }}
),
rookie_league_seasons AS
(
    SELECT *
    FROM {{  ref('int_player_rookie_league_seasons')  }}
),
rookie_nhl_seasons AS
(
    SELECT *
    FROM {{  ref('int_player_rookie_nhl_seasons')  }}
),
rookie_nhl_seasons2 AS
(
    SELECT *
    FROM {{  ref('int_player_rookie_nhl_seasons')  }}
),
rookie_tier_seasons AS
(
    SELECT *
    FROM {{ ref('int_player_rookie_tier_seasons')  }}
),
league_tiers AS
(
    SELECT * FROM {{  ref('league_tiers')  }}
),
final AS
(
    SELECT
        career_statistics.*,
        league_tiers.tier,
        CASE
            WHEN rookie_league_seasons.career_statistic_id IS NOT NULL THEN 'Y'
            ELSE 'N'
        END rookie_league_season_indicator,
        CASE
            WHEN rookie_nhl_seasons2.career_statistic_id = career_statistics.career_statistic_id THEN 'Y'
            ELSE 'N'
        END rookie_nhl_season_indicator,
        CASE
            WHEN career_statistics.season < rookie_nhl_seasons.season THEN 'Y'
            ELSE 'N'
        END pre_nhl_season_indicator,
        CASE
            WHEN rookie_tier_seasons.career_statistic_id IS NOT NULL THEN 'Y'
            ELSE 'N'
        END rookie_tier_season_indicator
    FROM career_statistics
    LEFT OUTER JOIN league_tiers
        ON career_statistics.league = league_tiers.league
    LEFT OUTER JOIN rookie_league_seasons
        ON career_statistics.career_statistic_id = rookie_league_seasons.career_statistic_id
    LEFT OUTER JOIN rookie_nhl_seasons
        ON career_statistics.player_url = rookie_nhl_seasons.player_url
    LEFT OUTER JOIN rookie_nhl_seasons2
        ON career_statistics.career_statistic_id = rookie_nhl_seasons2.career_statistic_id
    LEFT OUTER JOIN rookie_tier_seasons
        ON career_statistics.career_statistic_id  = rookie_tier_seasons.career_statistic_id
)
SELECT *
FROM final
WITH rookie_season AS
(
    SELECT
        player_url,
        league,
        MIN(season) rookie_season,
        MIN(career_statistic_id) rookie_season_career_statistic_id
    FROM {{ ref('stg_wikipedia__career_statistics') }}
    GROUP BY
        player_url,
        league
)
SELECT *
FROM rookie_season
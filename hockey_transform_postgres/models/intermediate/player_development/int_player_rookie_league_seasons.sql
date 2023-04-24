WITH final AS
(
    SELECT
        player_url,
        league,
        MIN(season) season,
        MIN(career_statistic_id) career_statistic_id
    FROM {{ ref('stg_wikipedia__career_statistics') }}
    GROUP BY
        player_url,
        league
)
SELECT *
FROM final
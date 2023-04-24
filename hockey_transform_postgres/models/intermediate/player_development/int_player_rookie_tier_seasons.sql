WITH final AS
(
    SELECT
        cs.player_url,
        lt.tier,
        MIN(season) season,
        MIN(career_statistic_id) career_statistic_id
    FROM {{ ref('stg_wikipedia__career_statistics') }} cs
    INNER JOIN {{  ref('league_tiers')  }} lt
        ON cs.league = lt.league
    GROUP BY
        cs.player_url,
        lt.tier
)
SELECT *
FROM final
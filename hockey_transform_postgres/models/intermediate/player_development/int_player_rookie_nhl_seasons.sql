WITH final AS
(
    SELECT
        player_url,
        MIN(season) season,
        MIN(career_statistic_id) career_statistic_id
    FROM {{ ref('stg_wikipedia__career_statistics') }}
    WHERE league = 'NHL'
    GROUP BY
        player_url
)
SELECT *
FROM final
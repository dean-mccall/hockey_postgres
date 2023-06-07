WITH leagues AS
(
    SELECT DISTINCT league
    FROM {{  ref('stg_wikipedia__career_statistics') }}
),
league_tiers AS
(
    SELECT *
    FROM {{ ref('league_tiers') }}
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
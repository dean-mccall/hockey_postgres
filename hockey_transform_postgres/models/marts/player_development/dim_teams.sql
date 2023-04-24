SELECT DISTINCT
    league,
    team
FROM {{ ref('stg_wikipedia__career_statistics') }}
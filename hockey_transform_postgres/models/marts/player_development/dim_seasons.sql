SELECT DISTINCT season
FROM {{ ref('stg_wikipedia__career_statistics') }}
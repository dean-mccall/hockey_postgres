SELECT career_statistic_id
FROM {{  ref('stg_wikipedia__career_statistics')  }}
WHERE NOT EXISTS
(
    SELECT 1
    FROM {{  ref('fact_career_statistics')  }}
)

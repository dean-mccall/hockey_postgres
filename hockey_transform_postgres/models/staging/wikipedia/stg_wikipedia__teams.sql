WITH cleaned_team AS
(
    SELECT
        team_id,
        team_url,
        CAST(REGEXP_REPLACE(league_conference, '[\u000a]', '', 'g') AS VARCHAR(255)) league_conference,
        CAST(REGEXP_REPLACE(conference_division, '[\u000a]', '', 'g') AS VARCHAR(255)) conference_division,
        CAST(REGEXP_REPLACE(team_name, '[\u000a]', '', 'g') AS VARCHAR(255)) team_name
    FROM {{ source('wikipedia','teams') }}
)
SELECT *
FROM cleaned_team
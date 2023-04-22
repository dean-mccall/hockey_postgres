SELECT * FROM wikipedia.players;

WITH cleaned_players AS
(
    SELECT 
        player_id,
        player_name,
        player_url,
        CAST(born AS DATE) born,
        CAST(height AS INTEGER) height_centimeters,
        ROUND((CAST(height AS INTEGER) * .393701), 2) height_inches,
        TRUNC(CAST(height AS INTEGER) * .393701 / 12) height_feet,
        CAST(TRUNC((CAST(height AS INTEGER) * .393701) / 12) AS VARCHAR)||' feet '||CAST(ROUND(((((CAST(height AS INTEGER) * .393701) / 12) - TRUNC((CAST(height AS INTEGER) * .393701) / 12))) * 12, 0) AS VARCHAR)||' inches' height_feet_and_inches, 
        CAST(weight AS INTEGER) weight_kilograms,
        ROUND(CAST(weight AS INTEGER) * 2.20462, 0) weight_pounds,
        position,
        shoots,
        national_team,
        nhl_draft,
        CASE 
            WHEN LENGTH(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(SPLIT_PART(nhl_draft, ',', 1), 'th overall', ''), 'rd overall', ''), 'nd overall', ''), 'Undrafted', ''), 'st overall', '')) = 0 THEN NULL
            ELSE CAST(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(SPLIT_PART(nhl_draft, ',', 1), 'th overall', ''), 'rd overall', ''), 'nd overall', ''), 'Undrafted', ''), 'st overall', '') AS INTEGER)
        END nhl_draft_position,
        CASE    
            WHEN LENGTH(SUBSTR(SPLIT_PART(nhl_draft, ',', 2), 1, 5)) = 0 THEN NULL
            ELSE CAST(SUBSTR(SPLIT_PART(nhl_draft, ',', 2), 1, 5) AS INTEGER)
        END nhl_draft_year,
        CASE
            WHEN LENGTH(SUBSTR(SPLIT_PART(nhl_draft, ',', 2), 6, LENGTH(nhl_draft))) = 0 THEN NULL
            ELSE CAST(SUBSTR(SPLIT_PART(nhl_draft, ',', 2), 6, LENGTH(nhl_draft)) AS VARCHAR(255))
        END nhl_draft_team,
        playing_career,
        CASE
            WHEN LENGTH(SPLIT_PART(REPLACE(playing_career, 'TBD', ''), '-', 1)) = 0 THEN NULL
            ELSE CAST(SPLIT_PART(REPLACE(playing_career, 'TBD', ''), '-', 1) AS INTEGER) 
        END playing_career_start_year,
        CASE
            WHEN SPLIT_PART(REPLACE(playing_career, 'TBD', ''), '-', 2) = 'present' THEN NULL
            ELSE CAST(SPLIT_PART(REPLACE(playing_career, 'TBD', ''), '-', 2) AS INTEGER)
        END player_career_end_year
    FROM wikipedia.players
)
SELECT *
FROM cleaned_players

SELECT *
FROM stg_wikipedia__players

SELECT 180 centimeters, 180 * .393701 inches, TRUNC((180 * .393701) / 12) feet, ROUND(((((180 * .393701) / 12) - TRUNC((180 * .393701) / 12))) * 12, 0)

SELECT COALESCE('1', NULL)

SELECT CAST(TRUNC((CAST(height AS INTEGER) * .393701) / 12) AS VARCHAR)||' feet '||CAST(ROUND(((((CAST(height AS INTEGER) * .393701) / 12) - TRUNC((CAST(height AS INTEGER) * .393701) / 12))) * 12, 0) AS VARCHAR)||' inches'
FROM wikipedia.players

SELECT *
FROM wikpedia.career_statistics

SELECT *
FROM wikpedia.career_statistics
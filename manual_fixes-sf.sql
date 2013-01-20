UPDATE meeting_search
SET "Meeting Title Link" = '/ga/Reno-GA/72930'
WHERE "Meeting Title Link" LIKE '%72930';

UPDATE meeting_search
SET "Meeting Title Link" = '/ga/Eunice-GA-There-is-a-Better-Way/72599'
WHERE "Meeting Title Link" LIKE '%72599';

UPDATE meeting_search
SET "Location Link" = '/locations/Oakland/Central-Office/45746'
WHERE "Location Link" LIKE '%45746';

UPDATE meeting_search
SET "Location Link" = '/locations/Reno-NV/-/29814'
WHERE "Location Link" LIKE '%29814';

UPDATE meeting_search
SET "Location Link" = '/locations/Gardnerville/-/29808'
WHERE "Location Link" LIKE '%29808';

-- Page doesn't display meeting information
INSERT INTO meeting_info (Url, "Meeting Description")
SELECT "Meeting Title Link", ''
FROM meeting_search WHERE "Meeting Title Link" LIKE '%//%';

INSERT INTO meeting_info (Url, "Meeting Description")
SELECT "Meeting Title Link", ''
FROM meeting_search WHERE "Meeting Title Link" LIKE '/naranon/%';

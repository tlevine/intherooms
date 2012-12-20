-- Newline in location link
UPDATE meeting_search
SET "Location Link" = '/locations/_/_/30016'
WHERE "Location Link" LIKE '%30016';

-- Newline in meeting link
UPDATE meeting_search
SET "Meeting Title Link" = '/ga/_/73215'
WHERE "Meeting Title Link" LIKE '%73215';

-- Page doesn't display meeting information
INSERT INTO meeting_info (Url, "Meeting Description") VALUES ('/oa//81760', '');

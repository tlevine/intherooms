SELECT "Location Link" FROM "meeting_search" WHERE "Location Link" NOT IN
  (SELECT "Url" FROM "location");
--SELECT "Meeting Title Link" FROM "meeting_search" WHERE "Meeting Title Link" NOT IN
--  (SELECT "Url" FROM "meeting_info");

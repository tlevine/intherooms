#!/bin/sh

sqlite3 intherooms.db -csv -header \
  "select '' AS 'Correct?', 'http://meetings.intherooms.com' || Url AS 'Url', [Meeting Description], Details, Format, Language, Phone from meeting_info order by random() limit 40;" > intherooms-meeting-sample.csv
sqlite3 intherooms.db -csv -header \
  "select '' AS 'Correct?', 'http://meetings.intherooms.com' || Url AS 'Url', Longitude, Latitude, [Location Description] from location order by random() limit 40;" > intherooms-location-sample.csv

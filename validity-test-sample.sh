#!/bin/sh

sqlite3 intherooms.db -csv -header 'select * from meeting_search order by random() limit 40;' > intherooms-meeting-sample.csv
sqlite3 intherooms.db -csv -header 'select * from location order by random() limit 40;' > intherooms-location-sample.csv

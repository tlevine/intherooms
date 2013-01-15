In The Rooms meetings database
===

I got locations from here.
http://meetings.intherooms.com/meetings/search

## Data
If you just want the data, you don't need to run anything. Download it as
[geojson](http://chainsaw.thomaslevine.com/intherooms.json),
[csv](http://chainsaw.thomaslevine.com/intherooms.csv) or
[sqlite](http://chainsaw.thomaslevine.com/intherooms.db).

The location information is normalized in the SQLite version. The "Meeting
Description" and "Location Description" fields can be structured more.

## How to run

First, activate

    . activate

Now, you can run any of the scripts.

    sqlite3 intherooms.db < schema.sql
    download_search.py [page number]
    download_meeting.sh [url]
    download_location.sh [url]
    parse_search.py intherooms.db [page number]
    parse_meeting.py intherooms.db [url]
    parse_location.py intherooms.db [url]

I made scripts for batch processing of the location and meeting pages.

    ./download_all_meetings.sh intherooms.db
    ./download_all_locations.sh intherooms.db
    ./parse_all_meetings.sh intherooms.db
    ./parse_all_locations.sh intherooms.db

Some manual fixes to weird pages are included.

    sqlite3 intherooms.db < manual_fixes.sql

Everything is wrapped up in one script.

    run

Generate a spreadsheet.

    sqlite3 -header -csv intherooms.db 'select * from meeting' > intherooms.csv

Or a geojson

    ./geojson.py intherooms.db > intherooms.json

Diagnose things

    ./counts.sh
    sqlite3 intherooms.db < todo.sql
    sqlite3 intherooms.db < interesting.sql
    sqlite3 intherooms.db 'SELECT page, count(*) FROM meeting_search GROUP BY page'

## Scope
robots.txt is good.

Questions
* Can we do without the additional meeting information for now
    (`/oa`, `/na`, &c. endpoints)? I think we need it.
* Can we do without the additional location information for now (`/locations`
    endpoint)? I think we don't need it; there often isn't any.)
* I think the MVP should not automatically update itself from In The Rooms;
    this will simplify the handling of errors.
* Are you fine with the resulting database being free and available to everyone
    in a convenient format?
* The search is weird. In particular, you only get 400 pages at once (easy to
    get around), and you need to specify a boundary on the location (annoying).
    It will be faster if we limit this to a few specific locations at first.
    Can we choose these?

I may request your help for writing test fixtures and for other less
specialized tasks.

Consider telling In The Rooms about the MVP as a way to convince them that
providing you with the data will be useful.


Everything I said is fine.

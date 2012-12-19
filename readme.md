Scrape locations from here.
http://meetings.intherooms.com/meetings/search

## How to run

First, activate

    . activate

Now, you can run any of the scripts.

    sqlite3 intherooms.db < schema.sql
    download_search [page number]
    download_meeting [url]
    download_location [url]
    parse_search intherooms.db [page number]
    parse_meeting intherooms.db [url]
    parse_location intherooms.db [url]

This is all wrapped up in one script.

    run

Generate a csv.

    sqlite3 -header -csv intherooms.db 'select * from meeting_search' > intherooms.csv

Diagnose things

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

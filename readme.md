In The Rooms meetings database
===

I got locations from here.
http://meetings.intherooms.com/meetings/search

## Report on the full dataset.
I have a complete-enough database of the In The Rooms meetings for
the continental United States. It also happens to include some
meetings in Mexico and Canada. It's [here](http://chainsaw.thomaslevine.com/intherooms.db).

The schema hasn't remarkably changed since when I explained it to
Samir before. I think that Addicaid needs only to concern itself
with the `meeting` view and the `location` table.

### Coverage
I accidentally deleted four of the meetings. If I run the job again
(not hard), I would get them back, but I don't think it's worth it.

That leaves 83760 meetings, of which 28 are broken on the In The
Rooms website, and 37293 locations, of which 5 are broken on the In
The Rooms website. This database thus contains 83732 meetings and
37288 locations.

### Correctness
I haven't reviewed this resulting dataset as much as I would like.
You could help with that by visiting the urls in these spreadsheets,
checking that the data in those urls match the data in the
spreadsheets, writing "yes" or "no" in the "Correct?" column and
then sending the result back to me.

* http://chainsaw.thomaslevine.com/intherooms-meeting-sample.csv
* http://chainsaw.thomaslevine.com/intherooms-location-sample.csv

In case you're curious, those spreadsheets are random samples.
https://github.com/tlevine/intherooms/blob/c73efa99c0e4ff772ed60d83b11a501f98d1991a/validity-test-sample.sh

### Tangential applications
I fixed some glaring errors in the In The Rooms information, so this
database cleaner in some ways than the one powering In The Rooms.
I wonder whether it could be helpful to In The Rooms.

Also, I'll probably eventually play with this dataset as I did
[with the New York data](http://thomaslevine.com/!/new-york-addiction-recovery-meetings/)

Tell me if there are any particular theories of addiction recovery
that I might be able to test or if there are any analyses that could
be useful to you.

### Logistics
Tell me if you think meeting in person would help. Or call me
whenever. I'm planning on going out of town this weekend and coming
back about a week after, but that's flexible.

## How to run

First, activate

    . activate

Now, you can run any of the scripts.

    sqlite3 intherooms.db < schema.sql
    ./download_searches.py
    ./download_meeting.sh [url]
    ./download_location.sh [url]
    ./parse_search.py intherooms.db [coordinates] [page number]
    ./parse_meeting.py intherooms.db [url]
    ./parse_location.py intherooms.db [url]

I made scripts for batch processing of the location and meeting pages.

    ./download_all_meetings.sh intherooms.db
    ./download_all_locations.sh intherooms.db
    ./parse_all_meetings.sh intherooms.db
    ./parse_all_locations.sh intherooms.db

Some manual fixes to weird pages are included.

    sqlite3 intherooms.db < manual_fixes.sql

Everything is wrapped up in one script.

    ./run

Generate a spreadsheet.

    sqlite3 -header -csv intherooms.db 'select * from meeting' > intherooms.csv

Or a geojson

    ./geojson.py intherooms.db > intherooms.json

Diagnose things

    ./counts.sh
    sqlite3 intherooms.db < todo.sql
    sqlite3 intherooms.db < interesting.sql
    sqlite3 intherooms.db 'SELECT page, count(*) FROM meeting_search GROUP BY page'
    ./validity-test-sample.sh

## Temporary notes
I accidentally deleted these records on the run of the week of February 25.
If I remove the `done-parsing` files and load the searches again, they will
come back, without tabs.

    [OrderedDict([(u'Meeting Title Link', u'/aa/ue\tpm0700-0800\tSpringfield-Study-Group\tSpringfield-\t/99181')]),
     OrderedDict([(u'Meeting Title Link', u'/alanon/\tOLD-TOWN-DAYTIME-AL-ANON/85924')]),
     OrderedDict([(u'Meeting Title Link', u'/na/Baja-Group--\t/85867')]),
     OrderedDict([(u'Meeting Title Link', u'/na/HOPE-II-\t/98904')])]

## Scope
The `robots.txt` permits crawling of the whole site.

    $ curl http://meetings.intherooms.com/robots.txt
    User-agent: *
    Allow: /

Here are my questions/considerations from when we first discussed this.

1. Can we do without the additional meeting information for now
    (`/oa`, `/na`, &c. endpoints)? I think we need it, and Addicaid agrees.
2. Do we need the additional location information for now (`/locations`
    endpoint)? Yes, mainly longitude and latitude.
3. The MVP will automatically update itself from In The Rooms; rather, the meetings
    will be imported from In The Rooms once, and we'll decide later whether and how
    to apply further updates.
4. Addicaid is fine with the resulting database being free and available to everyone
    in a convenient format?
5. The search is weird. In particular, you only get 400 pages at once (easy to
    get around), and you need to specify a boundary on the location (annoying).
    It will be faster if we limit this to a few specific locations at first.
    Can we choose these?
  * Tom started with New York.
  * Then Tom did San Francisco for the demo.
  * Then Tom did the whole country.
6. Tom may request Addicaid's help for writing test fixtures and for other less
    specialized tasks.
7. Consider telling In The Rooms about the MVP as a way to convince them that
    it will be useful for them to provide Addicaid with the data. (Addicaid
    had already contacted In The Rooms about getting the data, but they didn't
    hear back or something.)

## About In the Rooms
In the Rooms is run by
[Ken Pomerance](http://kenpomerance.com/)
("[Mr Clean](http://opencorporates.com/companies/us_fl/P06000144749)")
and RON "RT" TANNEBAUM
([two](http://100interviews.com/post/2050725736/71)
[interviews](http://www.recoverymonth.gov/Multimedia/Ask-the-Expert/Bio-Ronald-Tannebaum.aspx)).

Here are some more links

* [Open Corporates](http://opencorporates.com/companies/us_fl/P07000095303)
* [Corporation Wiki](http://www.corporationwiki.com/Florida/Plantation/ronald-d-tannebaum-P2117824.aspx)
* [Ken's Twitter](https://twitter.com/Mrclean1982)
* [Crunchbase](http://www.crunchbase.com/company/intherooms)

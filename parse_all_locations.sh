#!/bin/sh
db="$1"

set -e

# Parse the locations
locations_todo=$(sqlite3 "$1" 'SELECT DISTINCT "Location Link" FROM "meeting_search" WHERE "Location Link" NOT IN (SELECT "Url" FROM "location");')
for url in $locations_todo; do
    echo $url
    ./parse_location.py "$url"
done


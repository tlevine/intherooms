#!/bin/sh
set -e
db="$1"

# Download locations based on those pages
for location in $(sqlite3 "$db" 'SELECT "Location Link" FROM meeting_search'); do
    if [ ! -e $IN_THE_ROOMS_ROOT/locations/$(echo "$location" | cut -d/ -f4).html ]; then
        ./download_location.sh "$location"
        sleep 0s
    fi
done

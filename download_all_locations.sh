#!/bin/sh
set -e
db="$1"

# Download locations based on those pages
for location in $(sqlite3 "$db" 'SELECT "Location Link" FROM meeting_search'); do
    location_number=$(echo "$location" | cut -d/ -f5)
    if [ ! -e "$IN_THE_ROOMS_ROOT/locations/${location_number}.html" ]; then
        ./download_location.sh "$location" ||
        ./download_location.sh /locations/_/_/"$location_number"
        sleep 0s
    fi
done

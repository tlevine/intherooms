#!/bin/sh
set -e
db="$1"

# Download meetings based on those pages
for meeting in $(sqlite3 "$db" 'SELECT "Meeting Title Link" FROM meeting_search'); do
    if [ ! -e $IN_THE_ROOMS_ROOT/meetings/$(echo "$meeting" | cut -d/ -f4).html ]; then
        ./download_meeting.sh "$meeting"
        sleep 0s
    fi
done


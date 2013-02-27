#!/bin/sh
set -e
db="$1"

# Download meetings based on those pages
for meeting in $(sqlite3 "$db" 'SELECT "Meeting Title Link" FROM meeting_search'); do
    meeting_number=$(echo "$meeting" | cut -d/ -f4)
    if [ ! -e $IN_THE_ROOMS_ROOT/meetings/$meeting_number.html ]; then
        ./download_meeting.sh "$meeting" ||
        ./download_meeting.sh /_/_/"$meeting_number"
        sleep 0s
    fi
done


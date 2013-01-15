#!/bin/sh
db="$1"

set -e

# Parse the meetings.
meetings_todo=$(sqlite3 "$1" 'SELECT "Meeting Title Link" FROM "meeting_search" WHERE "Meeting Title Link" NOT IN (SELECT "Url" FROM "meeting_info");')
for url in $meetings_todo; do
    if ! ./parse_meeting.py "$url"; then
        echo "Error for $url"
        exit 1
    fi
done

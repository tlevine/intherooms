#!/bin/sh

c() {
    numerator=$(sqlite3 intherooms.db "select count(*) from [$1]") || return
    denominator=$(ls "$2"|wc -l)
    percent=$((100 * $numerator / $denominator))
    echo "$2: $numerator of $denominator ($percent%)"
}

c meeting_info meetings
c location locations

#!/bin/sh
set -e

# Activate
env|grep '^IN_THE_ROOMS_ROOT=' || . activate

# Go through pages
for page in $(seq 1 400); do
    # Skip things that have already been downloaded.
    [ -e "$IN_THE_ROOMS_ROOT/searches/$page.html" ] && continue

    # Download a webpage.
    ./download_search.py $page

    # Test that it worked.
    if ! grep '<span class="current">'$page'</span>' \
        "$IN_THE_ROOMS_ROOT/searches/$page.html" > /dev/null; then
        mv "$IN_THE_ROOMS_ROOT/searches/$page.html" .last.html
        echo I stopped at page $page. If the script worked properly, this is because
        echo page $(($page - 1)) was the last page. Check .last.html to make sure.
        exit
    fi

    sleep 8s
done

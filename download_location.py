#!/bin/sh
set -e

if ! env|grep '^IN_THE_ROOMS_ROOT='; then
    echo 'Not activated'
    exit 1
fi

if [ "$#" != '1' ]; then
    echo "USAGE: $0 [url]"
fi

url="$1"
_id=$(echo "$url"|cut -d/ -f5)

if [ -z "$_id" ]; then
    echo "The url $url has an empty id."
    exit 1
fi

wget -O "$IN_THE_ROOMS_ROOT/locations/${_id}".html "http://meetings.intherooms.com${url}"
echo Downloaded $url

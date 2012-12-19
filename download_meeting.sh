#!/bin/sh
set -e

if ! env|grep '^IN_THE_ROOMS_ROOT='; then
    echo 'Not activated'
    exit 1
fi

if [ "$#" != '1' ]; then
    echo "USAGE: $0 [url]"
fi

url=$(echo "$1"|sed 's_^/alanon/_/aa/_')
_id=$(echo "$url"|cut -d/ -f4)

if [ -z "$_id" ]; then
    echo "The url $url has an empty id."
    exit 1
fi

if [ -e "$IN_THE_ROOMS_ROOT/meetings/${_id}".html ]; then
    Already downloaded $url
else
    wget -O "$IN_THE_ROOMS_ROOT/meetings/${_id}".html "http://meetings.intherooms.com${url}"
    echo Downloaded $url
fi

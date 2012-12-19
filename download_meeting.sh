#!/bin/sh
set -e

if ! env|grep '^IN_THE_ROOMS_ROOT='; then
    echo 'Not activated'
    exit 1
fi

if [ "$#" != '1' ]; then
    echo "USAGE: $0 [url]"
fi

url=$(echo "$1"|sed -e 's_^/alanon/_/aa/_' -e 's_//_/-/_g')
_id=$(echo "$url"|cut -d/ -f4)

if [ -z "$_id" ]; then
    echo "The url $url has an empty id."
    exit 1
fi

echo $url
if [ -e "$IN_THE_ROOMS_ROOT/meetings/${_id}".html ]; then
    echo Already downloaded $url
else
    wget -O "$IN_THE_ROOMS_ROOT/meetings/${_id}".html "http://meetings.intherooms.com${url}"
    echo "Downloaded ${url}"
    sleep 0.5s
fi

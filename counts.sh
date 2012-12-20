#!/bin/sh

echo -n Meeting info:\ 
sqlite3 intherooms.db 'select count(*) from meeting_info'

echo -n Location:\ 
sqlite3 intherooms.db 'select count(*) from location'

#!/usr/bin/env python2
'''
This is a hack; move it into parse_meeting.py if I care.
'''
import re
import dumptruck

PHONE = re.compile(r'.*1?[^0-9]?([0-9]{3})[^0-9]?([0-9]{3})[^0-9]?([0-9]{4}).*')

dt = dumptruck.DumpTruck(dbname = 'intherooms.db')
for row in dt.execute('SELECT * FROM meeting_info'):
    if not row['Meeting Description']:
        continue

    # Number of colons
    ncolon = len(filter(lambda x: ':' in x, row['Meeting Description']))

    # Remove newlines
    desc = row['Meeting Description'].replace('\r', ' ').replace('\n', ' ')

    # Reset
    row['Details'] = row['Format'] = row['Language'] = row['Phone'] = ''

    phone = re.match(PHONE, desc)
    if phone:
        row['Phone'] = phone.group(1) + phone.group(2) + phone.group(3)
    elif len(filter(lambda c: c in '1234567890', desc)) >= 4:
        # Print it if it has four digits but wasn't matched.
        print row

    m3 = re.match(r'^Details: (.*)Format: (.*)Language: (.*)$', desc)
    m2 = re.match(r'^Details: (.*)(Format|Language): (.*)$', desc)
    m1 = re.match(r'^Details: (.*)$', desc)
    mweird = re.match(r'^Details: (.*)[fF]ormat:(.*)$', desc)
    if m3:
        row['Details'] = m3.group(1)
        row['Format'] = m3.group(2)
        row['Language'] = m3.group(3)
    elif m2:
        row['Details'] = m2.group(1)
        row[m2.group(2)] = m2.group(3)
    elif ncolon == 1 and m1:
        row['Details'] = m1.group(1)
    elif mweird:
        row['Details'] = mweird.group(1)
        row['Format'] = mweird.group(2)
    else:
        print desc
        assert False
    dt.upsert(row, 'meeting_info', commit = False)
dt.commit()

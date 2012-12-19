import os
import dumptruck
import lxml.html

def main():
    import sys
    filename = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'locations', _id(sys.argv[1])

    dt = dumptruck.DumpTruck(
        dbname = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'intherooms.db'),
        adapt_and_convert = True
    )


import os
import dumptruck
import lxml.html

cords = re.compile(r'var startPoint = new google.maps.LatLng\(([0-9.]+), (-[0-9.]+)\);')

def main():
    import sys
    filename = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'locations', _id(sys.argv[1])

    dt = dumptruck.DumpTruck(
        dbname = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'intherooms.db'),
        adapt_and_convert = True
    )


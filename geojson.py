#!/usr/bin/env python2

def features(dt):
    'Convert the database into geojson'
    out = []
    for row_in in dt.execute('SELECT * FROM meeting'):
        row_out = {
            "type": "Feature",
            "geometry": {
                "type": "Point", "__type": "GeoPoint",
                "coordinates": [row_in.pop('Longitude'), row_in.pop('Latitude')]
            },
        }
        row_out['properties'] = row_in
        out.append(row_out)
    return out


def main():
    import sys
    from dumptruck import DumpTruck
    from json import dumps
    db = sys.argv[1]
    dt = DumpTruck(dbname = db)
    f = features(dt)
    print dumps({
        "type": "FeatureCollection",
        "features": f
    })

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import cgi
import os
import sqlite3

DB_FILE = os.getenv("DB_FILE", "/var/lib/three-tier-db/clients.db")

print("Content-type:text/plain; charset=utf-8\n")

conn = sqlite3.connect(DB_FILE)
curs = conn.cursor()

form = cgi.FieldStorage()
querystring = form.getvalue("querystring")
if querystring is not None and querystring.strip() != "":
    queryval = "%" + querystring.strip() + "%"
    select = (
        "SELECT Planet, DistanceFromSunAU, Moons, DiameterMiles, MoonDetails, StarDetails "
        "FROM planets WHERE Planet LIKE ? ORDER BY DistanceFromSunAU ASC"
    )
    rows = curs.execute(select, (queryval,))
else:
    select = (
        "SELECT Planet, DistanceFromSunAU, Moons, DiameterMiles, MoonDetails, StarDetails "
        "FROM planets ORDER BY DistanceFromSunAU ASC"
    )
    rows = curs.execute(select)

for row in rows:
    if len(row) == 6:
        print("\t".join(str(item) for item in row))

conn.close()

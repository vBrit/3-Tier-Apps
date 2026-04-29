#!/usr/bin/env python3

import html
import os

import requests
from urllib.parse import parse_qs, quote_plus

DB_HOST = os.getenv("DB_HOST", "three-tier-db")
DB_PORT = os.getenv("DB_PORT", "8080")
ICON_BASE_PATH = "/usr/local/apache2/htdocs/icons"


def esc(value):
    return html.escape(str(value), quote=True)


def fmt_int(value):
    try:
        return f"{int(float(value)):,}"
    except Exception:
        return value


def fmt_au(value):
    try:
        return f"{float(value):.2f}".rstrip("0").rstrip(".")
    except Exception:
        return value


querystring = parse_qs(os.getenv("QUERY_STRING", "")).get("querystring", [""])[0]

url = f"http://{DB_HOST}:{DB_PORT}/cgi-bin/data.py"
if querystring:
    url = f"{url}?querystring={quote_plus(querystring)}"

print("Content-type:text/html; charset=utf-8\n")
print("<html><head><title>Planetary Database</title></head><body>")
print("<h1>Planetary Database</h1>")
print('<form action="/cgi-bin/app.py" method="get">')
print(f'<input type="text" name="querystring" value="{esc(querystring)}" placeholder="Filter planet">')
print('<button type="submit">Search</button>')
print('<a href="/cgi-bin/app.py">Clear</a>')
print("</form>")

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    rows = [line for line in response.text.splitlines() if line.strip()]
except Exception as exc:
    print(f"<p>Backend request failed: {esc(exc)}</p>")
    print("</body></html>")
    raise SystemExit

print("<table border='1' cellpadding='6' cellspacing='0'>")
print("<tr><th>Planet</th><th>Distance (AU)</th><th>Moons</th><th>Diameter (miles)</th></tr>")
for row in rows:
    parts = row.split("\t")
    if len(parts) < 4:
        continue
    planet, distance, moons, diameter = parts[:4]
    print("<tr>")
    print(f"<td>{esc(planet)}</td>")
    print(f"<td>{esc(fmt_au(distance))}</td>")
    print(f"<td>{esc(fmt_int(moons))}</td>")
    print(f"<td>{esc(fmt_int(diameter))}</td>")
    print("</tr>")
print("</table>")
print("</body></html>")

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_largest_technology_companies_by_revenue"
headers_req = {"User-Agent": "TeachingBot/1.0 (educational)"}
response = requests.get(url, headers=headers_req)
soup = BeautifulSoup(response.text, "html.parser")


def parse_table(table):
    """Parse a wikitable whether or not it uses <thead>."""
    # Get all rows
    all_rows = table.find_all("tr")
    if not all_rows:
        return [], []

    # First row is headers (works for most Wikipedia tables)
    header_cells = all_rows[0].find_all(["th", "td"])
    headers = [c.get_text(strip=True) for c in header_cells]

    # Remaining rows are data
    rows = []
    for tr in all_rows[1:]:
        cells = tr.find_all(["td", "th"])
        if len(cells) != len(headers):
            continue  # skip malformed rows
        rows.append([c.get_text(strip=True) for c in cells])

    return headers, rows


# --- Find the 2025 table specifically ---
h2 = soup.find("h2", id="2025_list")
print(f"Found heading: {h2.get_text(strip=True) if h2 else 'NOT FOUND'}")

table = h2.find_next("table", class_="wikitable")
headers, rows = parse_table(table)

print(f"\nHeaders ({len(headers)}): {headers}")
print(f"Data rows: {len(rows)}\n")

for row in rows:
    print(row)
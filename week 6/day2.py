import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_largest_technology_companies_by_revenue"
response = requests.get(url, headers={"User-Agent": "MyBot/1.0"})

soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table", id="mwBbg")
for table in tables:
    rows = table.find_all("tr")
    print(f"Table with {len(rows)} rows found.")

for row in rows:
    cells = row.find_all("td")
    data = [cell.get_text(strip=True) for cell in cells]
    print(data)


 
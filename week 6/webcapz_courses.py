import requests
from bs4 import BeautifulSoup
url = "https://www.webcapz.com/creative-agency-services/"
response = requests.get(url, headers={"User-Agent": "MyBot/1.0"})
soup = BeautifulSoup(response.text, "html.parser")
all_courses = []
course_lists = soup.find_all("div", class_="content-box")
for course_list in course_lists:
    courses = course_list.find_all("h5")
    for course in courses:
        title = course.get_text(strip=True)
        if title:
            if title == "Dedicated Team":
                continue
            all_courses.append(title)
print(all_courses)
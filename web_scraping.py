import requests
from bs4 import BeautifulSoup

# Make a request
page = requests.get(
    "https://www.topuniversities.com/university-rankings/world-university-rankings/2023/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title

# Extract body of page
page_body = soup.body

# Extract head of page
page_head = soup.head

# print the result
print(page_body)
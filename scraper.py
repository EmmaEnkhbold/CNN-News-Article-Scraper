import requests
from bs4 import BeautifulSoup

#CNN Articles Website
URL = "https://www.cnn.com/articles"

#retrieve the HTML content
request = requests.get(URL)
pageContent = request.content

#parse with BeautifulSoup object
soup = BeautifulSoup(pageContent, 'html.parser')

#find all headings on the page
headings = soup.find_all("h3")

#print the text of all headings
for i in headings:
    print(i.text)

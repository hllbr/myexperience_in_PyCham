import requests

from bs4 import BeautifulSoup
from requests.models import Response

url = "https://www.yemeksepeti.com/istanbul"

response: Response = requests.get(url)

html_icerik = response.content

soup = BeautifulSoup(html_icerik, "html.parser")
print(soup.find_all("div",{"class ":"banabi-delivery-info"}))
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi, "html.parser")
a =float(input("Rating'i giriniz : "))

baslıklar =soup.find_all("td", {"class":"titleColumn"})
ratinkler = soup.find_all("td",{"class":"ratingColumn imdbRating"})
for baslık,ratink in zip(baslıklar,ratinkler):
    baslık=baslık.text
    ratink=ratink.text
    baslık=baslık.strip()
    baslık=baslık.replace("\n","")
    ratink=ratink.strip()
    ratink=ratink.replace("\n","")
    if(float(ratink)>a):
        print("film ismi {} filmin ratingi {}".format(baslık,ratink))
   # print("Baslık",baslık)
    #print("Rating",ratink)




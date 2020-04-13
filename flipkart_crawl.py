import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree"
source = requests.get(url)

soup = BeautifulSoup(source.content, "html.parser")
data = soup.findAll('div',{'class':'_3wU53n'})
for d in data:
    print(data)
    print()

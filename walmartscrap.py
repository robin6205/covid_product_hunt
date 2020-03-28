from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('scrapetable.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product','availability','Price','Location'])

source = requests.get('https://www.walmart.com/store/2414/cary-nc/search?query=toilet%20papers').text

soup = BeautifulSoup(source, 'lxml')


title = soup.find('div', class_ = 'tile-title').div.text
print(title)
#title = soup.find('div', class_ = 'tile-in-store-info')['aria-label']
#txttitle = f'{title}'
#print(txttitle)
for item in soup.find_all('div', class_="search-result-wrapper"):
    avail = item.find('div', class_ = 'tile-in-store-info').text
    title = item.find('div', class_ = 'tile-title').div.text
    address = item.find('span', class_ = 'store-type-name').find_all(text=True)
    price =
    #.find_all(text=True, recursive=False)
    print(avail.prettyfy())

    csv_writer.writerow([title,avail,price,address])
csv_file.close()

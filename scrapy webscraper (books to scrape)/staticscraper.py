from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd

pages = []
prices = []
stars = []
titles = []
urls = []

#pages_to_scrape = int(input("Enter number of pages to scrape : "))
pages_to_scrape = 1
for i in range(1,pages_to_scrape+1):
    url = ('https://books.toscrape.com/catalogue/page-{}.html').format(i)
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = bs4(page.text, 'html.parser')
    #print(soup)
    for i in soup.find_all('h3'):
        ttl = i.getText()
        titles.append(ttl)
        #print(ttl)
    for j in soup.find_all('p', class_ ='price_color'):
        price = j.getText()
        prices.append(price)
        print(price)
    for s in soup.find_all('p',class_ = 'star-rating'):
        for k,v in s.attrs.items():
            star = v[1]
            stars.append(star)
            print(star)
    divs = soup.find_all('div', class_ = 'image_container')
    for thumbs in divs:
        tgs = thumbs.find('img', class_ = 'thumbnail')
        url = 'https://books.toscrape.com/'+ str(tgs('src'))
        #newurl = url.replace("../", "")
        #urls.append(newurl)
        print(url)


d = {"Tittle":titles , "Prices": prices, 'Star':stars, 'Image-url': urls}
#print(data)
#df = pd.DataFrame(data = d)
#df.index+=1
#df.to_excel("E:/Projects/scrapped excel sheet/sample.xlsx")
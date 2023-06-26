# This program scrapes web info
# The example used is retrieving the price of an item from an Amazon link
import bs4, requests

def getPrice(url):
    res = requests.get(url,headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
        'Accept-Language': 'en-US'
    })
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#corePrice_feature_div > div > span > span.a-offscreen')
    thePrice = elems[0].text.strip()
    return thePrice
    
price = getPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922')
print('The price is ' + price)


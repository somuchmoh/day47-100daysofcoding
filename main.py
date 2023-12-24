import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.myimaginestore.com/airpod/airpods-pro-2nd-g"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi-IN;q=0.8,hi;q=0.7"
}

page = requests.get(URL, headers=header).content

soup = BeautifulSoup(page, "lxml")
price = soup.find(name="span", class_="price").text
product = soup.find(name="span", class_="base").text

price_num = int(price.split("₹")[1].replace(",", ""))

if price_num > 23000:
    print(f"The price of {product} is below ₹25,000. Current price is {price}.")
else:
    print(price)

import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/Sceptre-24-5-inch-DisplayPort-Speakers-C255B-FWT240/dp/B0BTKJFRDV/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.4b335ede-a344-46a5-af28-95a1242a7034&dib=eyJ2IjoiMSJ9.3glZjBc6B5SxGupTsYPIOMs8EkdFuZWrsETBaMb2L4wKEjDh334Ctg2rsm2uIJ21varZhNOuPBtAyJokInSfhgtrroCmjgPmyMkHRjIvVa29qfCICBII61Z6rL0Pr-XU9O-8-qBxfBy9rHOvhjXbMwgE-o-jHaqfGaF-e-2Zts9zXWh6pkNnOto7rcYeTikTh_VOoQ31RCuOg910_7XyYedvI-2_JvsvJlsFYXdMu2jqQPKcvawXLuf7jgwonaCOw1f2Vh8cPYLzuErw0EvBFGOZsabI2MueNO0tQa0yyIQ.RTOVDnkmQ9CAW1aBGmBITX-3xkB5Z25O3J-RVIm509w&dib_tag=se&keywords=video%2Bgaming&pd_rd_r=b63b6394-597b-4d15-ad25-2cdeb1c79cad&pd_rd_w=Ebl9Q&pd_rd_wg=mVTgx&pf_rd_p=4b335ede-a344-46a5-af28-95a1242a7034&pf_rd_r=2T9STX83WWZER3TNXEP1&qid=1722519112&sr=8-2&th=1'
response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')


title_data = soup.find("span",attrs={"id": 'productTitle'})
title = title_data.string.strip()

print(f"Product title: {title}")


first_price = soup.find("span",class_="a-size-mini a-color-secondary aok-nowrap a-text-strike").text

print(f"First price: {first_price}")

discount = soup.find("span",class_="a-size-medium-plus _product-comparison-desktop_priceStyle_savings-percent__3-qzG").string

print(f"Discount: {discount[1:]}")

last_price = soup.find_all("span",class_="a-offscreen")[1].text

print(f"Last price: {last_price}")


total_reviews = soup.find("span",attrs={"id" : "acrCustomerReviewText"}).text[:6]

print(f"Total reviews: {total_reviews}")

rating_info = soup.find("span",attrs={"id": 'acrPopover'})
rating = rating_info.text.strip()[4:]

print(f"Product rating:{rating}")

availability = soup.find("span",class_="a-color-attainable").text

print(f"Availability: {availability}")

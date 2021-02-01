import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.ca/Computer-Leather-Executive-Ergonomic-Headrest/dp/B07PVK37SF/ref=sr_1_5?dchild=1&keywords=gaming+chair&qid=1612164682&sr=8-5'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[0:5])

    if (converted_price < 1700):
        send_mail()

    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('minecraftnoob381@gmail.com', 'password')

    subject = "Price fell down!"
    body = 'Check the amazon link https://www.amazon.ca/Sony-ILCE7M2K-Mirrorless-28-70mm-Compact/dp/B00PX8CNCM/ref=sr_1_2?dchild=1&keywords=sony+a7&qid=1612162717&sr=8-2'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'minecraftnoob381@gmail.com',
        msg
    )

    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


while(True):
    check_price()
    time.sleep(60 * 60)
